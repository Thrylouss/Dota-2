import React, { useRef } from "react";
import './pages.css';
import World from '/world-of-dota-2.jpg';
import { ScrollAnimation } from "../features/ScrollAnimation/ScrollAnimation.jsx";
import FirstSection from "../components/MainSections/FirstSection.jsx";
import NewsSection from "../components/MainSections/NewsSection.jsx";
import SecondSection from "../components/MainSections/SecondSection.jsx";
import {GetHeroes} from "../features/GetHeroes/GetHeroes.jsx";
import Carousel from "../features/Carousel/Carousel.jsx";
import About from "../components/About/About.jsx";
import Footer from "../components/Footer/Footer.jsx";

export default function MainPage() {
    const text = useRef();
    const secondText = useRef()
    const { heroes } = GetHeroes({page: 1});

    const { isVisible: showText } = ScrollAnimation({ element: text });
    const { isVisible: showSecondText } = ScrollAnimation({ element: secondText });

    const first = {
        section: text,
        showText: showText,
        first_head: 'Join the',
        second_head: 'Battle of the Ancients',
        text: 'Every day, millions of players worldwide enter the ' +
            'battle as one of over a hundred Dota Heroes in a 5v5 team clash. ' +
            'Dota is the deepest multi-player action RTS game ever made and there\'s ' +
            'always a new strategy or tactic to discover. It\'s completely free to play ' +
            'and always will be – start defending your ancient now.',
        image: 'https://cdn.akamai.steamstatic.com/apps/dota2/images/dota_react//home/radiant_dire5.jpg',
        button_text: 'See What\'s New',
        button_link: '/news',
    }
    const second = {
        section: secondText,
        showText: showSecondText,
        first_head: 'Who Will You',
        second_head: 'Choose?',
        text: 'From magical tacticians to fierce brutes and cunning rogues,\n' +
            'Dota 2\'s hero pool is massive and limitlessly diverse.\n' +
            'Unleash incredible abilities and devastating ultimates on your way to victory.',
        image: World,
        button_text: 'View All Heroes',
        button_link: '/heroes',
    }


    return (
        <>
            <div className='main-container'>
                <FirstSection/>
            </div>
            <div className='main-news-container'>
                <NewsSection/>
            </div>
            <div>
                <SecondSection info = {first}/>
            </div>
            <div>
                <SecondSection info = {second}/>
            </div>
            <div className='main-heroes-icons'>
                <Carousel heroes={GetHeroes({page: 1}).heroes} side={true}/>
                <Carousel heroes={GetHeroes({page: 2}).heroes} side={false}/>
                <Carousel heroes={GetHeroes({page: 3}).heroes} side={true}/>
                <Carousel heroes={GetHeroes({page: 4}).heroes} side={false}/>
                <Carousel heroes={GetHeroes({page: 5}).heroes} side={true}/>
                <div className='vinete'></div>
            </div>
            <div className='main-about'>
                <About/>
            </div>
            <Footer/>
        </>
    )
}