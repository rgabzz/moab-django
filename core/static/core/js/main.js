// Seletor de skin (Tack Zone X-5 e futuros produtos com skin).
// Cada pagina que tem um seletor de skin define `window.skinData` antes deste
// script rodar (ver bloco "skin_data_script" nos templates). Se a pagina nao
// tiver nenhum ".swatch" (produto sem skin), este trecho simplesmente nao faz nada.

document.querySelectorAll('.swatch').forEach(btn => {
  btn.addEventListener('click', () => {
    const skin = btn.dataset.skin;
    const data = (window.skinData || {})[skin];
    if (!data) return;

    document.querySelectorAll('.swatch').forEach(s => s.classList.remove('active'));
    btn.classList.add('active');

    document.querySelectorAll('.skin-img').forEach(img => {
      img.classList.toggle('active', img.dataset.skin === skin);
    });

    const nameEl = document.getElementById('skinName');
    const descEl = document.getElementById('skinDesc');
    const badgeEl = document.getElementById('skinBadge');

    if (nameEl) nameEl.textContent = data.name;
    if (descEl) descEl.textContent = data.desc;
    if (badgeEl) badgeEl.textContent = data.badge;
  });
});
