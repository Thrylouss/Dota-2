import damage from "../../../public/icons/icon_damage.png";
import time from "../../../public/icons/icon_attack_time.png";
import range from "../../../public/icons/icon_attack_range.png";


export default function CurrentHeroAttack({hero}) {
    return (
        <div className='current-hero-atack'>
            <h2>Attack</h2>
            <div>
                <img src={damage} alt=""/>
                <p>{hero.hero && hero.hero.attack.damage}</p>
            </div>
            <div>
                <img src={time} alt=""/>
                <p>{hero.hero && hero.hero.attack.attack_rate}</p>
            </div>
            <div>
                <img src={range} alt=""/>
                <p>{hero.hero && hero.hero.attack.attack_range}</p>
            </div>
        </div>
    )
}