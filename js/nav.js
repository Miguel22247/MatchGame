const home = document.querySelector('#home');
const feature = document.querySelector('#features');
const about = document.querySelector('#about');
const demo = document.querySelector('#demo');
const team = document.querySelector('#team');
const contact = document.querySelector('#contact');


home.addEventListener('click', (e) => {
    e.preventDefault();
    window.scroll({ top: 0, left: 0, behavior: 'smooth' });
});
feature.addEventListener('click', (e) => {
    e.preventDefault();
    window.scroll({ top: 350, left: 0, behavior: 'smooth' });
});
demo.addEventListener('click', (e) => {
    e.preventDefault();
    window.scroll({ top: 800, left: 0, behavior: 'smooth' });
});
about.addEventListener('click', (e) => {
    e.preventDefault();
    window.scroll({ top: 1200, left: 0, behavior: 'smooth' });
});
team.addEventListener('click', (e) => {
    e.preventDefault();
    window.scroll({ top: 1750, left: 0, behavior: 'smooth'});
});
contact.addEventListener('click', (e) => {
    e.preventDefault();
    window.scroll({ top: 2000, left: 0, behavior: 'smooth' });
});
