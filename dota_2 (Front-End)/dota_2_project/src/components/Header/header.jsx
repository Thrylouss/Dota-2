import logo from '/dota2_logo_horiz.png'
import {Link} from "react-router-dom";
import '../components.css'
import {SteamButton} from "../../UI/SteamButton/SteamButton.jsx";

export default function Header(){


    return (
        <header>
            <div className='header-content'>
                <ul className='nav-bar'>
                    <li>
                        <Link to='/'><img src={logo} alt=""/></Link>
                    </li>
                    <li>
                        <Link to='/heroes'>Heroes</Link>
                    </li>
                </ul>
            </div>
            <SteamButton />
        </header>
    )
}