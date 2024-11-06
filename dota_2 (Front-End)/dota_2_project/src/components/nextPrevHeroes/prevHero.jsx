import HeroAttr from "../CurrentHero/Hero_attr.jsx";
import {useRef} from "react";

export const PrevHero = ({hero}) => {
    const urlPrevHero = `/heroes/${hero?.name}`
        const prevVideoRef = useRef(null);
    const handlePrevMouseEnter = () => {
        if (prevVideoRef.current) {
            prevVideoRef.current.play()
        }
    }

    const handlePrevMouseLeave = () => {
        if (prevVideoRef.current) {
            prevVideoRef.current.pause()
        }
    }
    return (
        <div className='next-heroes prev' onClick={() => window.location.href = urlPrevHero}
             onMouseEnter={handlePrevMouseEnter}
             onMouseLeave={handlePrevMouseLeave}>
            {hero.video && (
                <video className='video' autoPlay loop muted preload='auto'
                       ref={prevVideoRef}>
                    <source src={hero.video} type='video/webm'/>
                </video>
            )}
            <div className='textHero prevText'>
                <h5 style={{color: 'gray'}}>NEXT HERO</h5>
                <h1>{hero?.name?.toUpperCase()}</h1>
                <span className={'hero-attr'}>
                    <div className="attrImg">
                       {hero?.main_attribute && <HeroAttr name={false} id={hero?.main_attribute}/>}

                    </div>
                    <h4>{hero?.attack_type?.toUpperCase()}</h4>
                </span>
            </div>

        </div>
    )
}