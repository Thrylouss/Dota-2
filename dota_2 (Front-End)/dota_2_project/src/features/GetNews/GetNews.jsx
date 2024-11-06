import {useEffect, useState} from "react";
import axios from "axios";


export const GetNews = () => {
    const [miniNews, setMiniNews] = useState([])

    useEffect(()=> {
        axios.get('http://localhost:8000/api/v1/news')
            .then(res => {
                setMiniNews(res.data.results.slice(0, 3))
            })
    }, [])

    return {miniNews}
}