import HeroAttr from "../CurrentHero/Hero_attr.jsx";
import {useRef} from "react";

export const NextHero = ({hero}) => {
    const urlNextHero = `/heroes/${hero?.name}`
    const nextVideoRef = useRef(null)
    const handleNextMouseEnter = () => {
        if (nextVideoRef.current) {
            nextVideoRef.current.play()
        }
    }
    const handleNextMouseLeave = () => {
        if (nextVideoRef.current) {
            nextVideoRef.current.pause()
        }
    }

    return (
        <div className='next-heroes next' onClick={() => window.location.href = urlNextHero}
                       onMouseEnter={handleNextMouseEnter}
                        onMouseLeave={handleNextMouseLeave}
        >

            <div className='textHero nextText'>
                <h5 style={{color: 'gray'}}>NEXT HERO</h5>
                <h1>{hero?.name?.toUpperCase()}</h1>
                <span className={'hero-attr'}>
                    <div className="attrImg">
                       {hero?.main_attribute && <HeroAttr name={false} id={hero?.main_attribute}/>}

                    </div>
                    <h4>{hero?.attack_type?.toUpperCase()}</h4>
                </span>
            </div>
            {hero.video && (
                <video className='video' loop muted preload='auto'
                       ref={nextVideoRef}>
                    <source src={hero.video} type='video/webm'/>
                </video>
            )}
        </div>
    )
}