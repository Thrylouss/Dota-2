import {useEffect, useState} from "react";
import axios from "axios";


export default function HeroAttr({id, name=true}){

    const [attr, setAttr] = useState('')

    useEffect(()=> {
        const fetchHero = async () => {
            try {
                await axios.get(`http://localhost:8000/api/v1/attributes/${id}`)
                    .then(res => {
                        setAttr(res.data)
                    })
            }
            catch (e) {
            }
        }

        fetchHero()

    }, [id])

    return (
        <div className='hero-attr'>
            {attr && (
                <>
                    <img src={attr.icon} alt=""/>
                    {name && <h2>{attr.name}</h2>}
                </>
            )}
        </div>
    )
}