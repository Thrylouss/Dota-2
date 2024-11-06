import HeroesFilter from "./heroes-filter.jsx";
import HeroesList from "./Heroes-list.jsx";
import {useState} from "react";


export default function HeroesMain(){
    const [selectedAttribute, setSelectedAttribute] = useState(0)
    const [selectedComplexity, setSelectedComplexity] = useState(0)
    const [searchedHero, setSearchedHero] = useState('')

    return (
        <div>
            <HeroesFilter
                setAttr={setSelectedAttribute}
                attr={selectedAttribute}
                setComplexity={setSelectedComplexity}
                comp={selectedComplexity}
                searchHero={setSearchedHero}/>
            <HeroesList
                attr={selectedAttribute}
                complexity={selectedComplexity}
                searchedHero={searchedHero}
            />
        </div>
    )
}