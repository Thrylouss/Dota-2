export default function AspectsCard({ aspect }) {
    return (
        <div className='current-aspects-card'>
            <div className='aspect-header'>
                <img src={aspect.icon} alt="" />
                <p>{aspect.title}</p>
            </div>
            <div className='current-aspects-info'>
                <p>{aspect.description}</p>
                {aspect.ability_description && (
                    <div className='aspect-skills'>
                        <img src={aspect.ability_icon} alt=""/>
                        <p>{aspect.ability_name}</p>
                    </div>
                )}
                <p dangerouslySetInnerHTML={{__html: aspect.ability_description}}/>
            </div>
        </div>
    );
}
