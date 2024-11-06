import './aspects.css'
import {GetCurrentAspects} from "../../features/GetCurrentHeroAspects/GetCurrentHeroAspects.jsx";
import AspectsCard from "./Aspects_card.jsx";

export default function CurrentHeroAspects({hero}){
    const aspects = GetCurrentAspects({id: hero.id})

    return (
        <div className='current-hero-aspects'>
            {aspects && aspects.map(aspect => {
                return <AspectsCard key={aspect.id} aspect={aspect}/>
            })}
        </div>
    )
}