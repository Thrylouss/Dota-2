import {useEffect, useState} from "react";
import melee from "../../../public/attack_type/melee.svg";
import ranged from "../../../public/attack_type/ranged.svg";


export default function HeroType({hero,show,setShow}){


    const handleClick = () => {
        setShow(!show)
    }


    return (
        <>
            <div className='hero-description'>
                <h1>{hero.name}</h1>
                <h2>{hero.advice}</h2>
                {show ? (<p className='full-history-hero' dangerouslySetInnerHTML={{__html: hero.history}}/>) : <p dangerouslySetInnerHTML={{__html: hero.description}}/>}

            </div>
            <p className='full-history' onClick={(e) => handleClick(e)}>{show ? 'Hide Full History' : 'Read  Full History'}</p>

            <h2>attack type</h2>
            <div className='hero_attack_type'>
                {hero.attack_type === 'melee' ? (
                    <>
                        <img src={melee} alt=""/>
                        <h2>Melee</h2>
                    </>
                ) : (
                    <>
                        <img src={ranged} alt=""/>
                        <h2>Ranged</h2>
                    </>
                )}
            </div>
            <h2>complexity</h2>
            <div className='hero-complexity'>
                <div className='comp comp-active'></div>
                <div className={`comp ${hero.complexity === (2 || 3) ? 'comp-active' : ''}`}></div>
                <div className={`comp ${hero.complexity === 3 ? 'comp-active' : ''}`}></div>
            </div>
        </>
    )
}