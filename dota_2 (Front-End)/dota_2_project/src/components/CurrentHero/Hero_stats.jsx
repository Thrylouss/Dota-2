import CurrentHeroAttack from "./Current_hero_attack.jsx";
import CurrentHeroDefense from "./Current_hero_defense.jsx";
import CurrentHeroMobility from "./Current_hero_mobility.jsx";

export default function HeroStats(hero){

    return (
        <div className='current-hero-type'>
            <CurrentHeroAttack hero={hero}/>
            <CurrentHeroDefense hero={hero}/>
            <CurrentHeroMobility hero={hero}/>
        </div>
    )
}