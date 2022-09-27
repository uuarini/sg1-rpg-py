#------------------------------------------------------------------------------
import pprint
races = ['ATUREN', 'HUMAN', 'JAFFA', 'TOKRA', 'UNAS']
classes = ['DIPLOMAT', 'ENGINEER', 'MEDIC', 'SCIENTIST', 'SCOUT', 'SOLDIER']
class_choice = 'unselected'
'''______________________________________________________________
|     _______________     _______________          _         |
|     |             |     |             |         / |        |
|     |                   |                      /  |        |
|     |                   |                         |        |
|     |______________     |     _________           |        |
|                   |     |             |           |        |
|                   |     |             |           |        |
|     |             |     |             |           |        |
|     |_____________|     |_____________|        ___|___     |
|____________________________________________________________|'''
print(f'''COMTRYA!
Welcome to the Stargate SG-1 Roleplaying Game Character Creator.
Choose a race: {races}.
Type 'info' for more on each race.''')
race = str.upper(input())
while True:
    if race in races:
        break;
    elif race == 'INFO':
        print('Which race do you want to learn about?')
        race_info = str.upper(input())
        break;
    else:
        print('DOES NOT COMPUTE. Try again.')
        race = str.upper(input())
while (race == 'INFO'):
    while class_choice != 'Y' or 'N':
        if race_info == 'ATUREN':
            print('''ATUREN:\nThe ATUREN, newly created for this game, are, to
    most, a newfound race hailing from an ancient
    civilization that lived in seclusion for tens of
    thousands of years. Their species was once similar
    to HUMANity, in trying to aggressively colonize
    their world, and their Great Houses warred over
    resources. This all came to an end when the Nox
    revealed themselves to the ATUREN and aspired to
    teach them a better way. The ATUREN, weary of
    the conflicts that had too long occupied them,
    were grateful for the Nox’s assistance and with
    their help started a path towards enlightenment.\n
    The ATUREN dedicated themselves to studying the
    great philosophy of peace and non-interference
    that the Nox live by, though they are far from
    perfect students. The Houses of the ATUREN do
    their best to settle their differences through debate
    and their Parliament. Some ATUREN have continued
    to practice the martial ways of their ancestors.
    They have not needed to engage in combat with
    others since the Nox came and uplifted their
    species, but they train and practice in case the
    day comes when it is needed.\n
    Using a gift from the Nox to shield their homeworld
    from prying eyes, the ATUREN were spared from the
    ravages of the System Lords until recently when a
    Tok’ra scout ship crash landed on a moon in their
    solar system. Unwilling to leave the Tok’ra agent
    to die, the ATUREN broke their promise of
    noninterference and took up the struggle against the
    Goa’uld. Now the ATUREN are preparing for war,
    while the Nox silently look on as their children join
    the struggle to free the galaxy from oppression.
    The ATUREN have allied themselves with the Tau’ri
    and their alliance at Phoenix Site, and though
    they do not have much to offer militarily, they
    have pledged the full support of their science
    and engineering breakthroughs.\n
    Their society is not organized by nationality but by
    which House an ATUREN belongs to. Though there
    are thousands of smaller Houses spread across
    Atura, there are 5 Great Houses which control
    most of ATUREN society. Each is based around
    their own interpretation of the Creed, which is
    the philosophy based around the teachings that
    the Nox tried to impart to the ATUREN. The Great
    Houses have been at peace with each other for
    centuries, though as the ATUREN open themselves
    up to the galaxy, once more old feuds have
    reawakened the bitter enmity between them. For
    now, they have kept their focus on their conflict
    with the System Lords, but the Nox fear for what
    will become of their children as they stray further
    away from their teachings.\nWould you like to choose ATUREN? enter y or n''')
            race_choice = str.upper(input())
            if race_choice == 'Y':
                race = 'ATUREN'
                break;
            elif race_choice == 'N':
                print('Which race do you want to learn about?')
                race_info = str.upper(input())
        elif race_info == 'HUMAN':
            print('''HUMAN:\nLife on Earth began in the primordial oceans,
    slowly evolving into the upright biped of the
    modern era. Millennia ago, the Goa’uld System
    Lord Ra arrived on Earth and used his technology to
    fool the citizens of Ancient Egypt into worshiping
    him as a god. Ra was eventually forced to leave
    Earth after his slaves revolted. By then he had
    exported millions of his followers off-world. The
    HUMANs were so useful to the System Lords, they
    bred them for use as hosts for the Goa’uld, and
    to seed various worlds throughout the galaxy.\n
    Little more than tools of the Goa’uld, the
    transplanted HUMANs had no opportunity to revive
    their native culture and often lived knowing only
    submission to their overlord. Some planets had
    little value to the Goa’uld after the establishment
    of HUMAN settlements and these supplicants were
    left to fend for themselves, often thriving as their
    natural curiosity and drive were left unchecked.\n
    On Earth HUMANs made their first unescorted
    journey into the greater Milky Way when the
    ancient Stargate was uncovered, almost ten
    millennia after the first HUMANs were enslaved.
    Under the direction of the United States Air Force,
    special teams were sent through the Stargate on
    exploratory missions. Even after so many years
    apart, the Tau’ri found other HUMANs who were
    virtually indistinguishable from themselves. The
    members of SG-1 witnessed the cruelty and
    tyranny of the Goa’uld and were not content to
    simply explore, but instead work to liberate the
    oppressed.\nWould you like to choose HUMAN? enter y or n''')
            race_choice = str.upper(input())
            if race_choice == 'Y':
                race = 'HUMAN'
                break;
            elif race_choice == 'N':
                print('Which race do you want to learn about?')
                race_info = str.upper(input())
        elif race_info == 'JAFFA':
            print('''JAFFA:\nAt first glance, JAFFA appear as their ancestors
    did when they were taken from their homes in
    Ancient Egypt – strong, capable, and proud. But
    like their forebears, the JAFFA live in subjugation.
    When the first HUMAN devotees were taken to the
    Goa’uld Queen on Dakara, she saw great potential
    in them – as incubators for her children. There
    the Queen twisted the HUMAN genome to leave
    JAFFA hosts reliant on the Goa’uld for survival.\n
    As children, JAFFA live normally. However, the
    Goa’uld Queen engineered a fatal failure into their
    immune system that is triggered during the Age of
    Prata (roughly, the time of puberty), thus requiring
    a symbiote be implanted. The strongest stock are
    chosen for the Prim’ta ceremony. During this rite,
    an abdominal pouch is opened in the JAFFA, and
    their first symbiote is implanted. Within hours,
    the child’s natural immune system is permanently
    destroyed and replaced by the larval Goa’uld.\n
    Despite their co-dependence, a JAFFA cannot
    directly communicate with the symbiote within.
    The only form of communication is through
    Kelno’reem. This ritual deep meditation allows the
    symbiote to heal and cleanse the host’s body. For
    most JAFFA, this process is subconscious, although
    a few speak on a more direct level. Almost any
    illness or injury can be healed during this process.
    The larval Goa’uld release naquadah into a JAFFA’s
    bloodstream, granting the ability to control certain
    Goa’uld technology and also sense the presence
    of nearby naquadah.\n
    Fueled by biological manipulation, the JAFFA
    become fast and strong while their symbiote
    uses their body to grow. Male JAFFA typically serve
    the Goa’uld Armies, while female JAFFA remain
    on their homeworld, ready to defend it from
    outside forces. When a prim’ta matures, it must
    be removed from the pouch and implanted in a
    host. The JAFFA must be implanted with a new
    symbiote, within a few hours, in order to avoid
    death.\nWould you like to choose JAFFA? enter y or n''')
            race_choice = str.upper(input())
            if race_choice == 'Y':
                race = 'JAFFA'
                break;
            elif race_choice == 'N':
                print('Which race do you want to learn about?')
                race_info = str.upper(input())
        elif race_info == 'TOKRA':
            print('''TOK'RA:\nThe Tok’ra are a specific family of Goa’uld created
    by the Goa’uld Queen Egeria. In opposition to
    the tyranny of the System Lord Ra, she instilled
    compassion in the genetic memory of her Prim’ta
    and named them the Tok’ra – a name meaning
    “against Ra.” In retaliation for the creation of the
    Tok’ra, System Lord Ra had Queen Egeria removed
    from her host and imprisoned for thousands of
    years, leaving the Tok’ra without any new prim’ta.\n
    Queen Egeria was discovered on the planet Pangar
    where new prim’ta were used by locals to create
    Tretonin, though she died soon after the SG-1
    team obtained samples of the drug. These samples
    would lead to the eventual invention of synthetic
    Tretonin for the JAFFA. While Queen Egeria left
    the JAFFA with the means to escape Goa’uld
    domination, her greatest weapon against them,
    the Tok’ra, will eventually become extinct without
    her, as they cannot create new larval Goa’uld.\n
    Tok’ra are unwilling to enslave their hosts and
    believe they should live communally, sharing one
    body. While Goa’uld take their hosts in whatever
    manner may be convenient, Tok’ra prefer to enter
    through a host’s mouth, thereby minimizing any
    exterior deformation. Tok’ra may race_choice a host
    based on convenience, curiosity, or kindness.
    After a Tok’ra has been removed from a host,
    there are no adverse impacts, although the host
    will continue to have naquadah in their blood
    and be able to sense it nearby. Most Tok’ra
    technology relies on the presence of naquadah
    in the bloodstream to activate.\n
    The youngest Tok’ra are from Pangar and were
    created with a flaw that prevents the production
    of Tretonin, which also resulted in the loss of their
    genetic memory. Some have chosen to remain on
    Pangar and continue the life they built with their
    hosts before the arrival of SG-1; however more
    found that the Goa’uld are a foe worth fighting.\n
    To this day, though they are of the same species,
    Tok’ra do not identify as Goa’uld and consider
    the Tau’ri allies against the System Lords. When
    General Loyer set up the Phoenix Site, he
    approached the Tok’ra for assistance. Seeing this
    as an opportunity to weaken the Goa’uld System
    Lords, several Tok’ra agreed to lend their aid in
    intelligence, logistics, and even as operatives on
    Phoenix Site teams.\nWould you like to choose TOK'RA? enter y or n''')
            race_choice = str.upper(input())
            if race_choice == 'Y':
                race = 'TOKRA'
                break;
            elif race_choice == 'N':
                print('Which race do you want to learn about?')
                race_info = str.upper(input())
        elif race_info == 'UNAS':
            print('''UNAS:\nThe UNAS evolved on the same homeworld as
    the Goa’uld and became their first hosts. With
    natural strength and regenerative abilities which
    could be further enhanced, they served the System
    Lords as enforcers and laborers. Use of the UNAS
    quickly fell out of favor with the System Lords
    when the introduction of HUMAN hosts provided
    a wider range of vocalization and higher manual
    dexterity. HUMANs quickly replaced them as the
    preferred host; however, primal Goa’uld still infest
    the waters of P3X-888, threatening resident UNAS.\n
    While the UNAS lack the vocal range of HUMANs,
    they are capable of mimicking some words and
    phrases, and their language is not so divergent
    as to prevent communication. Many linguists,
    building on the works of Dr. Daniel Jackson, have
    race_infoed enough of the language to communicate
    with them. Through the concerted efforts of
    various Stargate teams, an alliance with several
    tribes of UNAS from P3X-888 was forged, and the
    brightest UNAS – those who have shown promise
    in understanding the Tau’ri language – have joined
    the Phoenix Site in the fight against the Goa’uld.\n
    Those who remain behind keep the old ways of
    their ancestors. They form small tribal communities
    which are led by a single dominant UNAS, typically
    a male. Younger UNAS are given tasks to complete
    as a rite of passage, which often involves venturing
    forth into the world to provide for the tribe. Even
    with the improved communication between UNAS
    and Stargate Command, little is known about the
    internal structure of the tribes, but in contrast
    to their beastly appearance, the UNAS show high
    levels of empathy and creativity.\n
    UNAS are reptilian in nature, with bulky bodies,
    large hands, and green blood. While they have
    greater regenerative abilities than a Tau’ri, they
    are not invulnerable and can succumb to high
    amounts of damage. They do not carry any
    naquadah in their system and neither do the
    primal Goa’uld threatening their planet.\nWould you like to choose UNAS? enter y or n''')
            race_choice = str.upper(input())
            if race_choice == 'Y':
                race = 'UNAS'
                break;
            elif race_choice == 'N':
                print('Which race do you want to learn about?')
                race_info = str.upper(input())
        else:
            print('DOES NOT COMPUTE. Try again.')
            race_info = str.upper(input())
print(f'''Your race is {race}.\nChoose a class: {classes}
Type 'info' for more on each class.''')
class1 = str.upper(input())
while True:
        if class1 in classes:
            break;
        elif class1 == 'INFO':
            print('Which class do you want to learn about?')
            class_info = str.upper(input())
            break;
        else:
            print('DOES NOT COMPUTE. Try again.')
            class1 = str.upper(input())
while (class1 == 'INFO'):
    while class_choice != 'Y' or 'N':
        if class_info == 'DIPLOMAT':
            print('''The Diplomat is charged with making peaceful contact
    with new civilizations and maintaining relationships with allied groups.
Would you like to choose Diplomat? enter y or n''')
            class_choice = str.upper(input())
            if class_choice == 'Y':
                class1 = 'DIPLOMAT'
                break;
            elif class_choice == 'N':
                print('Which class do you want to learn about?')
                class_info = str.upper(input())
        elif class_info == 'ENGINEER':
            print('''The Engineer maintains the wide range of technology used by the Phoenix Site.
Would you like to choose Engineer? enter y or n''')
            class_choice = str.upper(input())
            if class_choice == 'Y':
                class1 = 'ENGINEER'
                break;
            elif class_choice == 'N':
                print('Which class do you want to learn about?')
                class_info = str.upper(input())
        elif class_info == 'MEDIC':
            print('''The Medic is designated to keep their team healthy and combat-ready.
Would you like to choose Medic? enter y or n''')
            class_choice = str.upper(input())
            if class_choice == 'Y':
                class1 = 'MEDIC'
                break;
            elif class_choice == 'N':
                print('Which class do you want to learn about?')
                class_info = str.upper(input())
        elif class_info == 'SCIENTIST':
            print('''The Scientist investigates the mysteries of new worlds and lost cultures.
Would you like to choose Scientist? enter y or n''')
            class_choice = str.upper(input())
            if class_choice == 'Y':
                class1 = 'SCIENTIST'
                break;
            elif class_choice == 'N':
                print('Which class do you want to learn about?')
                class_info = str.upper(input())
        elif class_info == 'SCOUT':
            print('''The Scout keeps his team safe in the wilderness and behind enemy lines.
Would you like to choose Scout? enter y or n''')
            class_choice = str.upper(input())
            if class_choice == 'Y':
                class1 = 'SCOUT'
                break;
            elif class_choice == 'N':
                print('Which class do you want to learn about?')
                class_info = str.upper(input())
        elif class_info == 'SOLDIER':
            print('''The Soldier is tasked with keeping his team alive when inevitable danger looms.
Would you like to choose Soldier? enter y or n''')
            class_choice = str.upper(input())
            if class_choice == 'Y':
                class1 = 'SOLDIER'
                break;
            elif class_choice == 'N':
                print('Which class do you want to learn about?')
                class_info = str.upper(input())
        else:
            print('DOES NOT COMPUTE. Try again.')
            class_info = str.upper(input())
print(f'Your race is {race} and your class is {class1}.')
input('press enter to exit')
