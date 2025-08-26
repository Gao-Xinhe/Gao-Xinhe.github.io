
// Reveal-on-scroll, once per element
(() => {
  const els = document.querySelectorAll('.fade-up');
  if (!('IntersectionObserver' in window) || els.length === 0) {
    // Graceful fallback
    els.forEach(el => el.classList.add('in-view'));
    return;
  }
  const io = new IntersectionObserver((entries) => {
    for (const e of entries) {
      if (e.isIntersecting) {
        const el = e.target;
        const delay = parseFloat(el.dataset.delay || '0');
        setTimeout(() => el.classList.add('in-view'), Math.max(0, delay * 1000));
        io.unobserve(el);
      }
    }
  }, { threshold: 0.12 });
  els.forEach(el => io.observe(el));
})();
