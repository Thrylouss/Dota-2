from .models import Attribute, Role, News

attributes_data = {
    'Strength': 'attributes/hero_strength_pQTGzev.png',
    'Agility': 'attributes/hero_agility_QGOQUSP.png',
    'Intelligence': 'attributes/hero_intelligence_uuDfdj4.png',
    'Universal': 'attributes/hero_universal_7L5FmLd.png',
}
roles_data = [
    'Carry',
    'Support',
    'Nuker',
    'Disabler',
    'Jungler',
    'Durable',
    'Escape',
    'Pusher',
    'Initiator'
]
news = [
    {
        'title':"The International Grand Champions",
        'content':"""Congratulations to Team Liquid, Grand Champions at The International 2024. Dropping only three games throughout their championship run, this relentless Liquid squad washed away a field of fearsome contenders to resoundingly earn their place as the finest Dota team in the world.

Team Liquid's journey to the Aegis started smoothly with a pair of 2-0 series wins over Aurora and beastcoast, but a 0-2 showing against defending champions Team Spirit reminded everyone that the path to immortality is filled with formidable foes.

Their next opponent would only prove that point further. With Liquid holding a 1-0 advantage and the Upper Bracket almost within reach, underdogs BB Team ran away with the second match of their seeding set, threatening Liquid with a much more difficult Lower Bracket path. Undaunted, Liquid leveraged early action in game three to build an avalanching lead and ultimately secure their place in the Upper Bracket to begin the next stage.

Once there, the eventual champions never looked back. Their heroes were almost unkillable in a dominating 2-0 win over Xtreme Gaming, with only a single death amongst them in game two. Carrying that momentum forward, they opened their series on the main stage against Cloud9 with another stomp. Game two turned into a closer back-and-forth fight, but Liquid rode an epic late game teamwipe to victory and a place in the Upper Bracket Final against a familiar opponent — and constant obstacle in their path — the dangerous Gaimin Gladiators.

Flipping precedent, Liquid withstood Gaimin's early aggression and took the series 2-0, marching convincingly into the Grand Final. After Gaimin battled their way back for a rematch, Team Liquid took the chance to demonstrate that the results of the first matchup were no fluke. They dispatched their old nemesis in decisive 3-0 fashion to secure the Aegis and a place in Dota 2 history.

As bearers of the ultimate symbol of victory, these names shall forever be inscribed upon the Aegis of Champions:

2024 - Team Liquid
 Michael "miCKe" Vu
 Michał "Nisha" Jankowski
 Neta "33" Shapira
 Samuel "Boxi" Svahn
 Aydin "Insania" Sarkohi


Looking Back

We would like to once again thank all of the players, talent, and everyone in the Dota community for helping bring this global celebration to life. If you missed any of the tournament, or just want to relive the incredible plays, head over to the Dota 2 YouTube channel, where you can find replays of the entire tournament. You can also find a trove of photos from the event over on the Dota 2 Instagram and Dota 2 flickr.

Celebrate the Champions

Special Champion edition sticker capsules are now available for purchase for Team Liquid. Each capsule contains one sticker featuring miCKe, Nisha, 33, Boxi, Insania, or Team Liquid. 50% of all sales will go directly to Team Liquid.

The International Compendium

If you've still got some challenges to complete and rewards to claim in The International 2024 Compendium, there's a bit more time before it all wraps up. You can still snag additional levels for your Compendium until Tuesday, October 15th, and other goodies like supporters packs, talent bundles, and champion stickers will be available a few weeks longer.

Upcoming Hero and Crownfall Act IV

Also, in case you missed the trailer during The International, we announced Dota's next hero. Leader of the flightless, sworn enemy of Queen Imperia, and general troublemaker Kez will be joining the roster of Dota heroes when Crownfall Act IV releases.""",
        'image':"news/5d614dc7454bfde1701834ffc951eb194a3a55af.jpg",
        'date':'2024-09-21'
    },
    {
        'title':"The International is Here",
        'content':"""For five straight days, sixteen teams have slugged their way through the Playoffs, and eight teams have earned a coveted spot at the main event: Team Liquid, Cloud9, Tundra Esports and Gaimin Gladiators in the upper bracket, and BB Team, Team Falcons, Aurora Gaming and Xtreme Gaming in the lower bracket. 

Congratulations to all eight teams as they vie to capture the Aegis at The International — only at Copenhagen's Royal Arena, starting on the luckiest day of the year, Friday, September 13th!

Watching The International Live
Schedule
The International Pre-show starts at 9:30 AM CEST, with the Opening Ceremony starting at 10 AM CEST and the first match between BB Team and Team Falcons starting soon after. Click here for the full schedule.

Getting In
Arena doors open at 8 AM CEST daily, two hours before every day's first match at 10 AM CEST, Friday through Sunday. Be ready to scan your Ticketmaster pass to gain entry (you can save it to your Android/Apple phone wallet for convenience). Make sure to get it scanned again anytime you leave, so you can use the same pass to re-enter. 

Getting To The Royal Arena
Here are directions to the Royal Arena. There are Metro stations and a train station just a few minutes walk from the arena. Visit Rejseplanen.dk for timetables.

Crimson Witness Treasure Drops
Inside the venue, there are two locations where you can show your ticket and pick up that day's commemorative badge, one near the ground floor entrance and another near the first floor main entrance. Each day has a unique badge, and you'll have to link that day's badge to be eligible for Crimson Witness treasures, which will be dropped randomly for attendees with bound badges at the first blood of every game. This year’s event-exclusive treasure includes updated Immortal items for Night Stalker, Meepo, Disruptor, Luna and Templar Assassin!

Watching The International Online
If you're one of the millions of Dota fans around the globe planning to watch The International online, check out the list below. From Twitch to YouTube to SteamTV, The International will be streamed on multiple platforms in multiple languages.
English: Twitch, SteamTV, YouTube
Spanish: Twitch, Facebook, SteamTV, YouTube
Russian: Twitch, SteamTV,  YouTube
Chinese: Twitch, SteamTV, Bilibili

The Secret Shop
The Secret Shop has two separate storefronts this year, depending on what part of the globe you're buying from— We Are Nations offers both US deliveries and international deliveries, and Perfect World offers domestic China deliveries and international deliveries. The stores have different items, so be sure to check out both.

Get Caught Up
If you’d like to see how the top eight teams got to where they are in the standings, you can 
catch up on Playoffs matches here!""",
        'image':"news/19deca390e7d27a5d4f6237fea74d1034cd0a29c.jpg",
        'date':'2024-09-13'
    },
    {
        'title':"The International: Streams, Secret Shop, and More",
        'content':"""June has come and, as it tends to do, now left us, probably forever. You'd be forgiven for forgetting all about crowns and them falling dramatically from the heads of fantasy birds and just enjoying your summer — slowing down, taking it easy, having a picnic at the beach or just napping for a while in a hammock. Well, we hope you enjoyed it, because July has come roaring into all of our lives, and with it,  Crownfall Act III: The Frosts of Icewrack. In fact, the lazy, meandering intro to this blog post is probably all the lounging around your poor eyeballs are going to get. Even as this June-esque paragraph winds its way towards a rambling sun-dappled conclusion, Act III is ramping up, July-like, to be the most eventful act yet.

Act III comes with an entirely new overworld map, located in the frigid north. It has mysteries, no small number of monsters, quite a bit of snow, and one hell of a barroom brawl. (And, as always, some surprises you'll have to find on your own.) Act III also comes with the Crownfall Collector's Cache, featuring 16 of the highest-rated sets from the last community vote. 

If you've been playing along through Crownfall as each act releases and want to jump right in to the new Act III content, you can start with Act III's intro comic, The Dragon, following Shen and her allies as they land in Icewrack, searching for Kestrel and his army. If you want a refresher on how we got here, you can also read the Act I intro comic, Ascension Day, and the Act II intro, The Battle of Hell's Basin.

If you're just joining in now, this is your reminder that all of the previous acts are still available, and will remain so through to the end of Crownfall. Speaking of which, given how much the event has grown since we initially imagined it (and how much its still growing), we've also decided to extend the event end date to October.

We're looking forward to the final battle with Queen Imperia. We'll see you there.""",
        'image':"news/83657233dc34270782879cd84ba8e751c8cae906.png",
        'date':'2024-07-10'
    },
    {
        'title':"Crownfall Act III and Collector's Cache",
        'content':"""The best Dota players in the world have arrived in Copenhagen and the games are about to begin. That's right: The Road to TI's Group Stage is officially underway for The International 2024.

There's a lot of fun stuff to cover before the event starts, and not a lot of time, so we're gonna stop introducing the information and start the informing. Let's get to it.

Tournament Streams
Group Stage is always glorious chaos. This year, almost fifty games will be played in the first two days alone, spread across three streams for each of the four official broadcast languages:
English: Twitch: Stream A, Stream B, Stream C; SteamTV: Stream A, Stream B, Stream C; YouTube: All Streams
Spanish: Twitch: Stream A, Stream B, Stream C; Facebook: All Streams; SteamTV: Stream A, Stream B, Stream C; YouTube: All Streams
Russian: Twitch: Stream A, Stream B, Stream C, Multi-Stream; SteamTV: Stream A, Stream B, Stream C, Multi-Stream; YouTube: All Streams
Chinese: Twitch: Stream A, Stream B, Stream C; SteamTV: Stream A, Stream B, Stream C; Bilibili: Stream A, Stream B, Stream C

After Group Stage wraps up, starting Friday, September 6th, both The Road to the International and The International itself will broadcast on one stream per official language:
English: Twitch, SteamTV, YouTube
Spanish: Twitch, FaceBook, SteamTV, YouTube
Russian: Twitch, SteamTV,  YouTube
Chinese: Twitch, SteamTV, Bilibili

If you're looking for unofficial languages, we've got those, too. We've handed out more than a dozen broadcast licenses, ranging from Bulgarian to Vietnamese, so check in with your local Dota community to find the best way to watch online.

And as always, anyone is welcome to join in on the streaming fun. We only ask that you follow our community streaming guidelines.

The Secret Shop
The International Secret Shop is once again open for business. We've got everything from mouse pads to jerseys to a real-life Toy Pudge plush, and so much more. There are two separate storefronts — We Are Nations offers both US deliveries and international deliveries, and Perfect World offers domestic China deliveries and international deliveries.

Tickets and Badges
Ground-floor tickets for The International have sold out, and even arena seats are mostly gone, but there are still a few left.

For attendees:
Your Ticketmaster ticket can be used for re-entry. Just remember to scan out as you leave so you can re-enter later in the day if you’d like.
Each day of the event, you'll get a new commemorative badge with a unique code that can be registered to your Steam account for potential Crimson Witness treasure drops. (The URL for registration is on the badge.)

What Else?
That's it for now. Honestly, that was a lot of information, and we're not going to lie, there might even be more on the way. But for now, don't worry about it. Just sit back, relax, and reread this blog post until you can recite it phonetically. We'll be calling everyone personally to verify you've got it memorized. You got this! Talk soon.""",
        'image':"news/b96eac3cc54c98b1c43b9ed1313cb7e36f4b6f71.jpg",
        'date':'2024-09-04'
    }
]


# class News(models.Model):
#     title = models.CharField(max_length=100)
#     content = models.TextField()
#     image = models.ImageField(upload_to='news/')
#     date = models.DateField(null=True, blank=True)

def data_loader():
    for key, value in attributes_data.items():
        Attribute.objects.create(name=key, icon=value)

    for role in roles_data:
        Role.objects.create(name=role)
    for new in news:
        News.objects.create(
            title=new['title'],
            content=new['content'],
            image=new['image'],
            date=new['date']
        )