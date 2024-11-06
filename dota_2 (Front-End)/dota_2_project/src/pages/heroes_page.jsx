import HeroesHeader from "../components/Heroes/Heroes-header.jsx";
import HeroesMain from "../components/Heroes/Heroes.jsx";
import Footer from "../components/Footer/Footer.jsx";


export default function Heroes(){

    return (
        <div className='heroes'>
            <HeroesHeader/>
            <HeroesMain/>
            <Footer/>
        </div>
    )
}