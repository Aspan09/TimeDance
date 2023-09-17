gsap.registerPlugin(ScrollTrigger, ScrollSmoother)

if (ScrollTrigger.isTouch !==1){
    // плавный скролл
    ScrollSmoother.create({
        wrapper: '.wrapper',
        content: '.content',
        smooth: 1.5,
        effects: true,
    })
}

    // прозрачность верхней части при прокрутке
    gsap.fromTo('.girl-fifth-page', { opacity: 1 }, {
        opacity: 0, 
        scrollTrigger:{
            trigger: '.girl-fifth-page',
            start: 'center',
            end: '790',
            scrub: true
        }
    })