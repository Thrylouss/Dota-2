import './hero-talents.css';

export default function CurrentHeroTalents({ hero }) {
    return (
        <div className='current-hero-talents'>
            <h1>Talents</h1>
            <div className='current-hero-talent'>
                {hero && Object.values(hero.talents).map((value, index) => (
                    <div className='span-talents' key={index}>

                        <span className='span-talent'>{value}</span>
                        {index % 2 === 1 && (
                            <div className="separator-border">
                                <div className='separator'>
                                    {index === 1 ? 25
                                        : index === 3 ? 20
                                            : index === 5 ? 15 : 10}
                                </div>
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    );
}
