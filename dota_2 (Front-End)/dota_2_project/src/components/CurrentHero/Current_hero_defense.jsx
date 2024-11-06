import armor from "../../../public/icons/icon_armor.png";
import mr from "../../../public/icons/icon_magic_resist.png";




export default function CurrentHeroDefense({hero}) {
    return (
        <div className='current-hero-atack'>
            <h2>Defense</h2>
            <div>
                <img src={armor} alt=""/>
                <p>{hero.hero && hero.hero.defense.armor}</p>
            </div>
            <div>
                <img src={mr} alt=""/>
                <p>{hero.hero && hero.hero.defense.magic_resistance}</p>
            </div>
        </div>
    )
}