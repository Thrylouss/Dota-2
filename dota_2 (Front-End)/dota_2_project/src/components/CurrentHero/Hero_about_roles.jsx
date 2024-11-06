import GetCurrentHeroRoles from "../../features/GetCurrentHeroRoles/GetCurrentHeroRoles.jsx";


export default function HeroAboutRoles({hero}){

    const heroRoles = GetCurrentHeroRoles(hero.id)

    return (
        <div className='hero-about-roles'>
            {heroRoles && heroRoles.map((role) => {
                return (
                    <div key={role.id} className='hero-about-role'>
                        <h4>{role.role.name}</h4>
                        <div><p style={
                            role.level === 0 ? {width: '0%'} :
                            role.level === 1 ? {width: '33%'} :
                            role.level === 2 ? {width: '66%'} :
                            {width: '100%'}
                        }></p></div>
                    </div>
                )
            })}
        </div>
    )
}