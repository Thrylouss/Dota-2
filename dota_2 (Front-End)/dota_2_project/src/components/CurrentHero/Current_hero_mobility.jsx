import ms from '../../../public/icons/icon_movement_speed.png'
import tr from '../../../public/icons/icon_turn_rate.png'
import vision from "../../../public/icons/icon_vision.png";

export default function CurrentHeroMobility({hero}) {

    return (
        <div className='current-hero-atack'>
            <h2>Mobility</h2>
            <div>
                <img src={ms} alt=""/>
                <p>{hero.hero && hero.hero.mobility.movement_speed}</p>
            </div>
            <div>
                <img src={tr} alt=""/>
                <p>{hero.hero && hero.hero.mobility.turn_rate}</p>
            </div>
            <div>
                <img src={vision} alt=""/>
                <p>{hero.hero && hero.hero.mobility.visibly}</p>
            </div>
        </div>
    )
}