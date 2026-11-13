/*
 * The deck: touch screens, and the help and introduction overlays.
 *
 * On a touch screen, the first tap on a room or container lights it up and
 * shows its picture, as hovering does with a mouse; a second tap (on it, or
 * on its picture) follows the link. With a mouse, the last room or container
 * pointed at stays lit until another is, or the pointer leaves the ship, so
 * its picture can be clicked too. Help and the introduction open in overlays
 * rather than new pages.
 */
(() => {
    const deck = document.querySelector('.deck');
    if (!deck) {
        return;
    }
    let pointer = 'mouse';
    const clear = () => {
        deck.querySelectorAll('.is-active').forEach(a => a.classList.remove('is-active'));
    };
    const light = slice => {
        if (!slice.classList.contains('is-active')) {
            clear();
            slice.classList.add('is-active');
        }
    };
    document.addEventListener('pointerdown', e => {
        pointer = e.pointerType;
        if (!e.target.closest('.deck .slice, .deck .preview')) {
            clear();
        }
    });
    // only when the pointer stays on it, not on its way across to a picture
    let resting;
    deck.addEventListener('pointerover', e => {
        const slice = e.target.closest('a.deck-room, a.deck-container');
        clearTimeout(resting);
        if (slice && e.pointerType === 'mouse') {
            resting = setTimeout(() => light(slice), 150);
        }
    });
    deck.addEventListener('pointerleave', e => {
        if (e.pointerType === 'mouse') {
            clearTimeout(resting);
            clear();
        }
    });
    deck.addEventListener('focusin', e => {
        if (e.target.matches('a.slice')) {
            clear();
        }
    });
    deck.addEventListener('click', e => {
        const slice = e.target.closest('a.slice');
        if (!slice) {
            return;
        }
        if (slice.dataset.overlay) {
            const dialog = document.getElementById('overlay-' + slice.dataset.overlay);
            if (dialog && dialog.showModal) {
                e.preventDefault();
                clear();
                dialog.showModal();
            }
            return;
        }
        if (pointer === 'touch' && slice.matches('.deck-room, .deck-container') && !slice.classList.contains('is-active')) {
            e.preventDefault();
            light(slice);
        }
    });
    // close an overlay by clicking outside it
    document.querySelectorAll('dialog.overlay').forEach(dialog => {
        dialog.addEventListener('click', e => {
            if (e.target === dialog) {
                const r = dialog.getBoundingClientRect();
                if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) {
                    dialog.close();
                }
            }
        });
    });
})();
