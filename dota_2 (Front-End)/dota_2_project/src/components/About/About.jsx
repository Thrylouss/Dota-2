import {ViewButton} from "../../UI/ViewButton/ViewButton.jsx";


export default function About(){

    return (
        <div className='about'>
            <div>
                <h1>JOIN</h1>
                <h1>BATTLE</h1>
            </div>
            <ViewButton blank={true} text={"PLAY FREE NOW"} link='https://store.steampowered.com/app/570/Dota_2/'/>
        </div>
    )
}