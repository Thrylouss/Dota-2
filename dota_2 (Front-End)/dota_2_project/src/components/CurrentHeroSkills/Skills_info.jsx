import React from 'react';

export default function SkillsList({ skill }) {
    let description = skill.description
    if (skill.scepter_description) {
        description = skill.scepter_description
    }
    else if (skill.shard_description) {
        description = skill.shard_description
    }
    let extra_desc = null
    if (skill.ability_has_scepter && skill.scepter_description) {
        extra_desc = "Scepter Ability Upgrade"
    }
    else if (skill.ability_has_shard && skill.shard_description) {
        extra_desc = "Shard Ability Upgrade"
    }
    else if (skill.ability_is_granted_by_scepter) {
        extra_desc = "Scepter Grants New Ability"
    }
    else if (skill.ability_is_granted_by_shard) {
        extra_desc = "Shard Grants New Ability"
    }
    return (
        <>
            <div className='skill-title'>
                <img src={skill.icon} alt={skill.name}/>
                <div className='skill-desc'>
                    <h2>{skill.name}</h2>
                    {extra_desc && <p className='extra_desc'>{extra_desc}</p>}
                    <p>{description}</p>

                </div>
            </div>
            <div className='skill-effect'>
                <h3>Spell Effects:</h3>
                {skill.spell_effects && (
                    <div className='spell-effects'>
                        {Object.entries(skill.spell_effects).map(([effectKey, effectValue]) => {
                            return(
                                <>
                                {effectValue && effectValue!=0 && <div key={effectKey}>
                                    <strong>{effectKey.replace(':', '').replaceAll('_', ' ')}:</strong> {/* Убираем двоеточие из ключа */}
                                    <span>{effectValue}</span> {/* Обработка null значений */}
                                </div>}
                                </>
                            )
                        })}

                    </div>
                )}
                <div className='skill-cost'>
                    {skill.cooldown != 0 && <p><strong>Cooldown:</strong> {skill.cooldown} seconds</p>}
                    {skill.mana_cost != 0 && <p><strong>Mana Cost:</strong> {skill.mana_cost}</p>}
                </div>
                {skill.tip && <p style={{color:'#888888'}}><strong>Tip:</strong> {skill.tip}</p>}
            </div>
        </>
    );
}
