(function () {
  function showToast(message) {
    var toast = document.querySelector("[data-toast]");
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add("visible");
    window.clearTimeout(showToast.timer);
    showToast.timer = window.setTimeout(function () {
      toast.classList.remove("visible");
    }, 2200);
  }

  document.querySelectorAll("[data-copy]").forEach(function (button) {
    button.addEventListener("click", function () {
      var text = button.getAttribute("data-copy") || "";
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(function () {
          showToast("Texte copié dans le presse-papiers.");
        }, function () {
          showToast(text);
        });
      } else {
        showToast(text);
      }
    });
  });

  document.querySelectorAll("[data-checklist]").forEach(function (list) {
    var meter = document.querySelector("[data-progress-meter]");
    var label = document.querySelector("[data-progress-label]");
    var checks = Array.prototype.slice.call(list.querySelectorAll("input[type='checkbox']"));
    function update() {
      var done = checks.filter(function (input) { return input.checked; }).length;
      var total = Math.max(checks.length, 1);
      var pct = Math.round(done / total * 100);
      if (meter) meter.style.setProperty("--progress", pct + "%");
      if (label) label.textContent = done + " / " + checks.length + " étapes validées";
    }
    checks.forEach(function (input) { input.addEventListener("change", update); });
    update();
  });

  document.querySelectorAll("[data-tablist]").forEach(function (tablist) {
    var root = tablist.closest("[data-tabs]");
    if (!root) return;
    var tabs = Array.prototype.slice.call(tablist.querySelectorAll("[data-tab]"));
    var panels = Array.prototype.slice.call(root.querySelectorAll("[data-panel]"));
    tabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        var target = tab.getAttribute("data-tab");
        tabs.forEach(function (item) {
          item.classList.toggle("primary", item === tab);
          item.setAttribute("aria-selected", item === tab ? "true" : "false");
        });
        panels.forEach(function (panel) {
          panel.hidden = panel.getAttribute("data-panel") !== target;
        });
      });
    });
  });
})();
