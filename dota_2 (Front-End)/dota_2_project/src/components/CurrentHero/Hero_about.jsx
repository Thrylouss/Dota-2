import HeroAboutAttr from "./Hero_about_attr.jsx";
import HeroAboutRoles from "./Hero_about_roles.jsx";
import HeroStats from "./Hero_stats.jsx";


export default function HeroAbout({hero}){

    return (
        <>
            <HeroAboutAttr hero={hero}/>
            {hero && <HeroAboutRoles hero={hero}/>}
            <HeroStats hero={hero}/>
        </>
    )
}