import numpy as np

openness = ['Openness to experience is a general appreciation for art, emotion, adventure, unusual ideas, imagination, curiosity, and variety of experience.',
            'People who are open to experience are intellectually curious, open to emotion, sensitive to beauty, and willing to try new things. They tend to be, when compared to closed people, more creative and more aware of their feelings. They are also more likely to hold unconventional beliefs. Open people can be perceived as unpredictable or lacking focus, and more likely to engage in risky behaviour or drug-taking. Moreover, individuals with high openness are said to pursue self-actualisation specifically by seeking out intense, euphoric experience.',
            'People with low openness want to be fulfilled by persevering and are characterised as pragmatic and data-driven, and sometimes even perceived to be dogmatic and closed-minded.']

conscientiousness = ['Conscientiousness is a tendency to be self-disciplined, act dutifully, and strive for achievement against measures or outside expectations. It is related to people\'s level of impulse control, regulation, and direction.',
                     'High conscientiousness is often perceived as being stubborn and focused. High conscientiousness indicates a preference for planned rather than spontaneous behaviour.',
                     'Low conscientiousness is associated with flexibility and spontaneity, but can also appear as sloppiness and lack of reliability.']

extraversion = ['Extraversion is characterised by breadth of activities , surgery from external activities or situations, and energy creation from external means.',
                'Extraverts enjoy interacting with people, and are often perceived as energetic. They tend to be enthusiastic and action-oriented. They possess high group visibility, like to talk, and assert themselves. Extraverts may appear more dominant in social settings, as opposed to introverts in that setting.',
                'Introverts have lower social engagement and energy levels than extraverts. They tend to seem quiet, low-key, deliberate, and less involved in the social world. Their lack of social involvement should not be interpreted as shyness or depression; but as greater independence of their social world than extroverts. Introverts need less stimulation, and more time alone than extroverts. This does not mean that they are unfriendly or antisocial; rather, they are aloof and reserved in social situations.']

agreeableness = ['Agreeableness is the general concern for social harmony.',
                 'Agreeable individuals value getting along with others. They are generally considerate, kind, generous, trusting and trustworthy, helpful, and willing to compromise their interests with others. Agreeable people also have an optimistic view of human nature.',
                 'Disagreeable individuals place self-interest above getting along with others. They are generally unconcerned with others\' well-being and are less likely to extend themselves to other people. Sometimes their skepticism about others\' motives causes them to be suspicious, unfriendly, and uncooperative. Disagreeable people are often competitive or challenging, which can be seen as argumentative or untrustworthy.']

neuroticism = ['Neuroticism is the tendency to have strong negative emotions, such as anger, anxiety, or depression. It is sometimes called emotional instability, or is reversed and referred to as emotional stability. Neuroticism is associated with low tolerance for stress or strongly disliked changes.',
               'Neurotic people are emotionally reactive and vulnerable to stress. They are more likely to interpret ordinary situations as threatening. They can perceive minor frustrations as hopelessly difficult. Their negative emotional reactions tend to stay for unusually long periods of time, which means they are often in a bad mood. Neurotic people may display more skin-conductance reactivity than calm and composed people. These problems in emotional regulation can make a neurotic person think less clearly, make worse decisions, and cope less effectively with stress. Being disappointed with one\'s life achievements can make one more neurotic and increase one\'s chances of falling into clinical depression. Neurotic individuals tend to experience more negative life events, but neuroticism also changes in response to positive and negative life experiences. Neurotic people tend to have worse psychological well-being.',
               'Less neurotic individuals are less easily upset and are less emotionally reactive. They tend to be calm, emotionally stable, and free from persistent negative feelings. Freedom from negative feelings does not mean that low scorers experience a lot of positive feelings; that is related to extraversion instead.']

def sample_discrete_normal_distribution(mean=3, std=1.0, size=1):
    """
    Sample from a normal distribution with specified mean and standard deviation,
    then round the samples to the nearest integer within the specified range [1, 5].
    """
    samples = np.random.normal(mean, std, size)
    samples = np.round(samples).clip(1, 5)
    return samples

def gen_personality():
    i1 =  int(sample_discrete_normal_distribution(mean=3, std=1.0, size=1)[0])
    i2 =  int(sample_discrete_normal_distribution(mean=3, std=1.0, size=1)[0])
    i3 =  int(sample_discrete_normal_distribution(mean=3, std=1.0, size=1)[0])
    i4 =  int(sample_discrete_normal_distribution(mean=3, std=1.0, size=1)[0])
    i5 =  int(sample_discrete_normal_distribution(mean=3, std=1.0, size=1)[0])

    description = ['very low', 'low', 'neutral', 'high', 'very high']

    i1p =  'You are a person with {} openness.'.format(description[i1-1])
    i2p =  'You are a person with {} conscientiousness.'.format(description[i2-1])
    i3p =  'You are a person with {} extraversion.'.format(description[i3-1])
    i4p =  'You are a person with {} agreeableness.'.format(description[i4-1])
    i5p =  'You are a person with {} neuroticism.'.format(description[i5-1])
        
    personality = openness[0] + openness[1] + openness[2] + i1p \
            + conscientiousness[0] + conscientiousness[1] + conscientiousness[2] + i2p \
            + extraversion[0] + extraversion[1] + extraversion[2] + i3p \
            + agreeableness[0] + agreeableness[1] + agreeableness[2] + i4p \
            + neuroticism[0] + neuroticism[1] + neuroticism[2] + i5p
    
    personality_debug =  i1p + i2p + i3p + i4p + i5p
    return personality, personality_debug