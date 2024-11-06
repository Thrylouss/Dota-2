import './skills-video.css';
import { useState, useEffect } from "react";
import HeroSkills from "../CurrentHero/Hero_skills.jsx";
import { CleanUrl } from "../../features/CleanUrl/CleanUrl.jsx";
import back from '../../../public/back.jpg';
import SkillsVideo from "./Skills_info.jsx";

export default function CurrentHeroSkillsVideo({ skills }) {
    const [currentSkill, setCurrentSkill] = useState(0);
    const [videoError, setVideoError] = useState(false);
    const [videoLoaded, setVideoLoaded] = useState(false);
    const [currentVideo, setCurrentVideo] = useState(null);
    useEffect(() => {
        const video = skills.find(skill => skill.number === currentSkill && !skill.is_facet);

        if (video) {
            setCurrentVideo(video);
            setVideoError(false);
        } else {
            let nextSkill = currentSkill + 1;
            while (nextSkill < skills.length) {
                const nextVideo = skills.find(skill => skill.number === nextSkill && !skill.is_facet);
                if (nextVideo) {
                    setCurrentSkill(nextSkill);
                    break;
                }
                nextSkill++;
            }
        }
    }, [currentSkill, skills]);

    useEffect(() => {
        setVideoError(false);
        setVideoLoaded(false);
    }, [currentVideo]);

    const handleVideoLoaded = () => {
        setVideoLoaded(true);
        setVideoError(false);
    };

    const handleVideoError = () => {
        console.log("Ошибка загрузки видео");
    };

    const cleanedUrl = currentVideo && currentVideo.video ? CleanUrl({ url: currentVideo.video }) : null;

    return (
        <div className='current-hero-skills-videos'>
            <div className='current-skills'>
                {cleanedUrl && !videoError ? (
                    <video
                        key={cleanedUrl}
                        autoPlay
                        loop
                        muted
                        preload='auto'
                        onLoadedData={handleVideoLoaded}
                        onError={handleVideoError}
                        playsInline
                    >
                        <source src={cleanedUrl} type='video/mp4' />
                    </video>
                ) : (
                    <img className='current-hero-img' src={back} alt="" />
                )}
                <div className='current-skills-icons'>
                    {skills && skills.map(skill => {
                        if (!skill.is_innate)
                            return (
                                <HeroSkills
                                    under={true}
                                    key={skill.id}
                                    skill={skill}
                                    setCurrentSkill={setCurrentSkill}
                                    currentSkill={currentSkill}
                                />
                            )
                    })}
                </div>
            </div>
            <div className='current-skill-info'>
                {currentVideo && <SkillsVideo skill={currentVideo} />}
            </div>
        </div>
    );
}
