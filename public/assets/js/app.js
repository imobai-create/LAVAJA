/* ==========================================================================
   LavaJá — comportamento do site. Sem dependências, sem build.
   Tudo que é preço/limite fica em CONFIG, para mudar em um lugar só.
   ========================================================================== */
(function () {
  "use strict";

  var CONFIG = {
    avulsa: 35,          // lavagem avulsa na máquina (R$)
    boxAvulso: 18,       // box de alta pressão, uso avulso (R$)
    planos: {
      essencial: { nome: "Essencial", preco: 59, lavagens: 4 },
      ilimitada: { nome: "Ilimitada", preco: 99, lavagens: Infinity },
      premium:   { nome: "Premium",   preco: 139, lavagens: Infinity }
    },
    precoFundador: 79,   // Ilimitada travada para os 80 primeiros
    vagasFundador: 80,
    whatsappPadrao: "5531987474828" // (31) 98747-4828 — atendimento provisório
  };

  var reduzMovimento = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var $ = function (s, ctx) { return (ctx || document).querySelector(s); };
  var $$ = function (s, ctx) { return Array.prototype.slice.call((ctx || document).querySelectorAll(s)); };
  var brl = function (v) {
    return v.toLocaleString("pt-BR", { style: "currency", currency: "BRL", maximumFractionDigits: 0 });
  };

  /* ---------- 1. origem da visita (UTM) ---------- */
  var ORIGEM = (function () {
    var guardado = {};
    try { guardado = JSON.parse(sessionStorage.getItem("lavaja_origem") || "{}"); } catch (e) { guardado = {}; }
    var q = new URLSearchParams(location.search);
    var novo = {
      source: q.get("utm_source") || guardado.source || "",
      medium: q.get("utm_medium") || guardado.medium || "",
      campaign: q.get("utm_campaign") || guardado.campaign || "",
      referrer: guardado.referrer || document.referrer || ""
    };
    try { sessionStorage.setItem("lavaja_origem", JSON.stringify(novo)); } catch (e) {}
    return novo;
  })();

  /* ---------- 2. cabeçalho ---------- */
  var header = $(".site-header");
  if (header) {
    var marcaHeader = function () { header.classList.toggle("fixa", window.scrollY > 12); };
    marcaHeader();
    addEventListener("scroll", marcaHeader, { passive: true });
  }

  /* ---------- 3. aparecer ao rolar ---------- */
  (function () {
    var alvos = $$(".reveal");
    if (!alvos.length) return;
    if (reduzMovimento || !("IntersectionObserver" in window)) {
      alvos.forEach(function (el) { el.classList.add("dentro"); });
      return;
    }
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add("dentro"); obs.unobserve(e.target); }
      });
    }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });
    alvos.forEach(function (el) { obs.observe(el); });
  })();

  /* ---------- 4. números que sobem ---------- */
  function contar(el, alvo, sufixo, duracao) {
    if (reduzMovimento) { el.textContent = alvo + (sufixo || ""); return; }
    var inicio = null, de = 0;
    duracao = duracao || 1200;
    function passo(t) {
      if (!inicio) inicio = t;
      var p = Math.min((t - inicio) / duracao, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(de + (alvo - de) * eased) + (sufixo || "");
      if (p < 1) requestAnimationFrame(passo);
    }
    requestAnimationFrame(passo);
  }
  (function () {
    var nums = $$("[data-contar]");
    if (!nums.length || !("IntersectionObserver" in window)) {
      nums.forEach(function (el) { el.textContent = el.getAttribute("data-contar") + (el.getAttribute("data-sufixo") || ""); });
      return;
    }
    var obs = new IntersectionObserver(function (entradas) {
      entradas.forEach(function (e) {
        if (!e.isIntersecting) return;
        contar(e.target, parseInt(e.target.getAttribute("data-contar"), 10), e.target.getAttribute("data-sufixo") || "");
        obs.unobserve(e.target);
      });
    }, { threshold: 0.6 });
    nums.forEach(function (el) { obs.observe(el); });
  })();

  /* ---------- 5. vagas de fundador ---------- */
  var whatsappNumero = CONFIG.whatsappPadrao;
  function aplicarWhatsapp(numero) {
    whatsappNumero = numero || whatsappNumero;
    $$("[data-zap]").forEach(function (a) {
      var texto = a.getAttribute("data-zap") || "Olá! Vim pelo site da LavaJá e quero saber mais.";
      a.href = "https://wa.me/" + whatsappNumero + "?text=" + encodeURIComponent(texto);
    });
  }

  function pintarVagas(d) {
    var restantes = typeof d.restantes === "number" ? d.restantes : CONFIG.vagasFundador;
    var limite = d.limite || CONFIG.vagasFundador;
    var usadas = Math.max(limite - restantes, 0);
    var elNum = $("#vagas-restantes");
    if (elNum) contar(elNum, restantes, "", 900);
    $$("[data-vagas-restantes]").forEach(function (el) { el.textContent = restantes; });
    $$("[data-vagas-limite]").forEach(function (el) { el.textContent = limite; });
    var barra = $("#barra-vagas");
    if (barra) setTimeout(function () { barra.style.width = Math.min((usadas / limite) * 100, 100) + "%"; }, 150);
    var reservadas = $("#vagas-reservadas");
    if (reservadas) reservadas.textContent = usadas + " já reservadas";
    if (d.esgotado || restantes <= 0) {
      $$("[data-se-esgotado]").forEach(function (el) { el.hidden = false; });
    }
  }

  function carregarStats() {
    fetch("/api/stats", { headers: { Accept: "application/json" } })
      .then(function (r) { return r.ok ? r.json() : Promise.reject(r.status); })
      .then(function (d) {
        pintarVagas(d);
        if (d.whatsapp) aplicarWhatsapp(d.whatsapp);
      })
      .catch(function () {
        // API fora do ar não pode quebrar a página: mostra o limite cheio.
        pintarVagas({ restantes: CONFIG.vagasFundador, limite: CONFIG.vagasFundador });
      });
  }
  aplicarWhatsapp(CONFIG.whatsappPadrao);
  if ($("#vagas-restantes") || $("[data-vagas-restantes]")) carregarStats();

  /* ---------- 6. calculadora de economia ---------- */
  (function () {
    var slider = $("#calc-lavagens");
    if (!slider) return;
    var base = "fundador";

    function atualizar() {
      var n = parseInt(slider.value, 10);
      var pct = ((n - slider.min) / (slider.max - slider.min)) * 100;
      slider.style.setProperty("--pct", pct + "%");
      $("#calc-n").textContent = n;
      $("#calc-n-label").textContent = n === 1 ? "lavagem por mês" : "lavagens por mês";

      var precoIlimitada = base === "fundador" ? CONFIG.precoFundador : CONFIG.planos.ilimitada.preco;
      var recomendado = n <= CONFIG.planos.essencial.lavagens
        ? { nome: "Essencial", preco: CONFIG.planos.essencial.preco }
        : { nome: "Ilimitada", preco: precoIlimitada };

      var avulso = n * CONFIG.avulsa;
      var economiaMes = avulso - recomendado.preco;

      $("#calc-avulso").textContent = brl(avulso);
      $("#calc-plano").textContent = brl(recomendado.preco);
      $("#calc-plano-nome").textContent = recomendado.nome + (recomendado.nome === "Ilimitada" && base === "fundador" ? " (fundador)" : "");
      $("#calc-economia").textContent = economiaMes > 0 ? brl(economiaMes) : brl(0);
      $("#calc-ano").textContent = economiaMes > 0 ? brl(economiaMes * 12) : brl(0);

      var veredito = $("#calc-veredito");
      if (economiaMes > 0) {
        veredito.textContent = "A partir de " + Math.ceil((recomendado.preco / CONFIG.avulsa) + 0.001) +
          " lavagens no mês a assinatura já sai mais barata que pagar avulso.";
      } else {
        veredito.textContent = "Com essa frequência, a lavagem avulsa a " + brl(CONFIG.avulsa) +
          " ainda compensa mais que assinar. A gente prefere te dizer isso agora.";
      }
    }

    slider.addEventListener("input", atualizar);
    $$("#calc-base button").forEach(function (b) {
      b.addEventListener("click", function () {
        base = b.getAttribute("data-base");
        $$("#calc-base button").forEach(function (o) { o.setAttribute("aria-pressed", String(o === b)); });
        atualizar();
      });
    });
    atualizar();
  })();

  /* ---------- 7. máscara de WhatsApp ---------- */
  $$("input[data-mascara=tel]").forEach(function (input) {
    input.addEventListener("input", function () {
      var d = input.value.replace(/\D/g, "").slice(0, 11);
      var out = d;
      if (d.length > 2 && d.length <= 7) out = "(" + d.slice(0, 2) + ") " + d.slice(2);
      else if (d.length > 7 && d.length <= 10) out = "(" + d.slice(0, 2) + ") " + d.slice(2, 6) + "-" + d.slice(6);
      else if (d.length > 10) out = "(" + d.slice(0, 2) + ") " + d.slice(2, 3) + " " + d.slice(3, 7) + "-" + d.slice(7);
      input.value = out;
    });
  });

  /* ---------- 8. formulários ---------- */
  function limparErros(form) {
    $$(".campo.erro", form).forEach(function (c) { c.classList.remove("erro"); });
  }
  function marcarErro(form, campo, texto) {
    var alvo = campo && $("#campo-" + campo, form);
    if (alvo) {
      alvo.classList.add("erro");
      var m = $(".erro-msg", alvo);
      if (m && texto) m.textContent = texto;
      var input = $("input,select,textarea", alvo);
      if (input) input.focus();
      return true;
    }
    return false;
  }

  function ligarFormulario(form) {
    if (!form) return;
    var endpoint = form.getAttribute("data-endpoint");
    var msg = $(".msg", form);
    var botao = form.querySelector("button[type=submit]");
    var textoBotao = botao ? botao.textContent : "";

    form.addEventListener("submit", function (ev) {
      ev.preventDefault();
      limparErros(form);
      msg.className = "msg";
      msg.textContent = "";

      var dados = {};
      new FormData(form).forEach(function (v, k) { dados[k] = typeof v === "string" ? v.trim() : v; });
      dados.consentimento = !!$("input[name=consentimento]", form).checked;
      dados.utm = { source: ORIGEM.source, medium: ORIGEM.medium, campaign: ORIGEM.campaign };
      dados.referrer = ORIGEM.referrer;

      if (!dados.consentimento) {
        marcarErro(form, "consentimento", "Precisamos da sua autorização para te chamar no WhatsApp.");
        return;
      }


      botao.disabled = true;
      botao.textContent = "Enviando…";

      fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json", Accept: "application/json" },
        body: JSON.stringify(dados)
      })
        .then(function (r) { return r.json().then(function (d) { return { ok: r.ok, status: r.status, d: d }; }); })
        .then(function (res) {
          if (res.ok) {
            msg.textContent = res.d.mensagem || "Recebemos seus dados. Falamos com você em breve.";
            msg.className = "msg ok";
            form.reset();
            if (form.id === "form-reserva") carregarStats();
            msg.scrollIntoView({ behavior: reduzMovimento ? "auto" : "smooth", block: "center" });
          } else {
            var texto = res.d.erro || "Não deu certo. Confira os dados e tente de novo.";
            // Erro de campo já aparece embaixo do input — não repetir na caixa geral.
            if (!marcarErro(form, res.d.campo, texto)) {
              msg.textContent = texto;
              msg.className = "msg ruim";
            }
          }
        })
        .catch(function () {
          msg.textContent = "Sem conexão agora. Tente de novo em instantes — ou fale direto no WhatsApp.";
          msg.className = "msg ruim";
        })
        .finally(function () {
          botao.disabled = false;
          botao.textContent = textoBotao;
        });
    });
  }
  $$("form[data-endpoint]").forEach(ligarFormulario);

  /* ---------- 9. barra fixa no celular ---------- */
  (function () {
    var barra = $(".barra-mobile");
    if (!barra) return;
    var formulario = $("#reservar");
    var ticking = false;

    function avaliar() {
      ticking = false;
      var passouDoHero = window.scrollY > window.innerHeight * 0.75;
      // Com o formulário na tela a barra só atrapalha: ela some.
      var formVisivel = false;
      if (formulario) {
        var r = formulario.getBoundingClientRect();
        formVisivel = r.top < window.innerHeight * 0.9 && r.bottom > 0;
      }
      barra.classList.toggle("visivel", passouDoHero && !formVisivel);
    }
    addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(avaliar); }
    }, { passive: true });
    addEventListener("resize", avaliar, { passive: true });
    avaliar();
  })();

  /* ---------- 10. ano no rodapé ---------- */
  $$("[data-ano]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
