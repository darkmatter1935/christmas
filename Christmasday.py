import streamlit as st
from datetime import date, timedelta

# ---------- CONFIG ----------
st.set_page_config(
    page_title="My attempt to make this Christmas a little more special <3",
    page_icon="🎄",
    layout="centered"
)

# ---------- PASSWORD PROTECTION ----------
PASSWORD = "7 janmo ke ache karam milake bhi i dont deserve you"

st.markdown("### 🔒 Private Space")
password_input = st.text_input(
    "Enter password jaanu ❤️",
    type="password"
)

if password_input != PASSWORD:
    if password_input:
        st.error("NOPE 😛 Think… something I wrote on it maybe?")
    else:
        st.caption("Hint: our polaroid 📸")
    st.stop()

# ---------- DATES ----------
START_DATE = date(2025, 12, 14)  # CHANGE if needed
TODAY = date.today()

# ---------- MESSAGES ----------
messages = [
    "❤️ **Day 1**\n\nHi Jaan, Im so grateful for you for being so sweet and making me that awesome amazing gift you did yesterday. I wanted to show you how much i appreciated you so i made this little thing. Everyday i wake up i feel grateful to have you in my life. youre my first thought in the morning and my last before i sleep jaan. Youre my favourite person my little sunflower. muahhhhhh",,
    "❤️ **Day 2**\n\nHi cutu, Today I wanted to tell you how Watching you sleep everyday makes me feel like the luckiest person alive. Im so grateful to have the privelege of seeing my beautiful princess drift off to dream world everynight. and everynight it feels the same - like someone melted my heart in a microwave.",,
    "❤️ **Day 3**\n\nHi baby, Today I wanted to tell you how GODAMN HOLY FUCKING GORGEOUS YOU AREE!!!! Like damn, baba sometimes i wonder ki mai hi pichle janam me mother teressa tha kya because theres absolutely no way in hell i ended up with someone as ABSOMINDFUCKINGLY angelic as you without divine intervention. Even if looking at you went I went to hell, i would stare at you with my whole soul and brag to the devil about being in heaven.",
    "❤️ **Day 4**\n\nHiiiiiiii my little cupcake, Today i wanted to tell you how the only thing i want for christmas, is youuuuuuuuuuuu. ever since you came in my life jaan, ive become a better person in all aspects of my life. i couldnt ask for anything more, because you are my everything, my love.",
    "❤️ **Day 5**\n\nHello madam ji, aaj maine socha aapko batau that i really really really admire how hardworking and dedicated you are in every little thing you do my love. everyday that i spend with you i get motivated to do more, and your passion and drive is genuinely so inspiring. i want you to know that even if no one believes in you, im right here standing by you jaan.",
    "❤️ **Day 6**\n\nNamaskaram Sundar Kanya, I thought i would tell you today how much i miss you every night that i sleep and wakeup. Every night i sleep hugging my pillow imagining its you, and somehow it calms my mind and makes the whole world go quiet. i cant wait to get married and hide you in my blanket for the whole day. i cant wait until you and i can sleep and wakeup together(although if we are together there isnt going to be any sleeping happeneing hehehehehehe), anyways Happy 19th my little baby, thank you for being with be all this while and i cant wait to spend the rest of my life with you. muahhhhh!",
    "❤️ **Day 7**\n\nHi my little cupcake, today i thought ill tell you about how hilarious you areeeeee, like sometimes you'll say the funniest things that i wont ever think of and youll make me laugh no matter how hard my day is going. i love how you make me smile everyday and i wouldnt have it any other ways. i lovelovelovelvoeloveyouuuuuuuu!",
    "❤️ **Day 8**\n\nHi jaanuuuuu, today i wanted to tell you how i loveeee you creative you are. your gifts are the most thoughtful and sweet gifts anyone has ever given me. wether they are your cards, or theyre your cookies that you bake, i love how creative you are in everything you do and how your mind works always amazes me",
    "❤️ **Day 9**\n\nHi swwetu, today i wanted to tell you how i could talk to you for hours and still feel like its not enough. even after 2.5 years i could talk to you about anything and everything and youre still the most interesting person to me. even though i know everything about you i still am the most interested in you. youre my favourite person my love, and i know you will be for the rest of my life.",
    "❤️ **Day 10**\n\nHi my little rudolph. Today i wanted to tell you how absolutely adorable you are, wether its you wrapped in your blanky like a little shawarma, or its you talking about how you fantasize about chicken taco mroe than me. youre the most adorable little baby in the whole wide worldddddd, and i will eat you up someday im not even kidding.",
    "🎄 **Day 11 – Christmas**\n\nMERRY CHRISTMAS JAANUUUUUUUUUUUUUUUUU, YOURE MY ONLY WISH FOR CHRISTMAS AND I LOVEEE YOUUUUUUUUUUUUUUU!!!!!!!!!!!!!!!!!!, MUAHHHHHHHHHHH ❤️"
]

# ---------- UI ----------
st.title("🎄 11 Days of Us")
st.subheader("Somethings I wanna tell you everyday")

# ❄️ Snowfall
st.snow()

st.write("Open **one gift per day** until Christmas.")
st.divider()

# ---------- CALENDAR ----------
for i in range(11):
    unlock_date = START_DATE + timedelta(days=i)

    if TODAY >= unlock_date:
        if st.button(f"🎁 Day {i+1}", key=f"day_{i}"):
            st.success(messages[i])
    else:
        st.button(f"🔒 Day {i+1}", disabled=True)

st.divider()
st.caption("Made with ❤️ just for you.")
