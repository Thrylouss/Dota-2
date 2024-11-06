import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import {BrowserRouter, Route, Routes} from "react-router-dom";
import Header from "./components/Header/header.jsx";
import MainPage from "./pages/main_page.jsx";
import Heroes from "./pages/heroes_page.jsx";
import News from "./pages/news_page.jsx";
import CurrentHero from "./components/CurrentHero/Current_hero.jsx";

createRoot(document.getElementById('root')).render(
      <>
          <BrowserRouter>
              <Header />

              <Routes>
                  <Route path="/*" element={<MainPage/>} />
                  <Route path="/heroes" element={<Heroes/>} />
                  <Route path="/heroes/:name" element={<CurrentHero/>} />
              </Routes>
          </BrowserRouter>
      </>
)
