import {Link} from "react-router-dom";
import MiniNewsCard from "../NewsCard/mini_news_cards.jsx";
import React from "react";


export default function NewsSection() {
    return (
        <>
            <div className='main-news-button'>
                <p>Latest News</p>
                <p><Link to='/news'>View All</Link></p>
            </div>
            <div className='main-news'>
                <MiniNewsCard/>
            </div>
        </>
    )
}