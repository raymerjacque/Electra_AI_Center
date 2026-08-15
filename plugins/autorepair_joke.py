<think>Got it, let's tackle this. First, the user asked for a joke in Turkish, right? The error says the Proactive Scanner can't handle joke requests. So we need a ROUTER plugin that triggers when someone asks for a joke, especially in Turkish? Wait, the request was "bana bir şaka yap" which is Turkish for "tell me a joke".

First, set the plugin metadata. PLUGIN_NAME should be something like "Şaka Yapıcı" (Joke Maker in Turkish) or "Joke Handler"? Wait, no, since the request is Turkish, maybe make the plugin name relevant. Wait, PLUGIN_TYPE is ROUTER, right? Because it's a capability gap for handling joke requests.

PLUGIN_TRIGGERS should include Turkish phrases for asking for a joke: "bana bir şaka yap", "şaka söyle", "bir şaka anlat", "şaka yap", maybe also English ones just in case? Like "tell me a joke", "say a joke". Oh right, to cover both.

PLUGIN_ROUTE_TOKEN should be something unique, like "JOKE" — wait, check if that's taken? The current installed plugins are none, so JOKE is fine. Wait, but make sure it's uppercase, no clashes. Yeah, JOKE is good.

PLUGIN_COMMANDS can be ["/joke", "/şaka"] to match both languages.

Then the run function. We need to return a joke, preferably in Turkish since the original request was Turkish, but maybe include some English ones too? Wait, no, the user asked in Turkish, so first respond with Turkish jokes, but maybe have a list. Also, make sure it's safe, no offensive jokes. Also, wrap in try/except so it doesn't crash.

Wait, also, the plugin needs to be named autorepair_joke.py right? Because the file is auto-named autorepair_<token_lowercase>.py, so token is JOKE, lowercase is joke, so filename is autorepair_joke.py, which matches.

Wait, let's structure the metadata first:

PLUGIN_NAME = "Şaka Yapıcı"  # Or "Joke Handler", but Turkish is better since the request was Turkish. Wait, but maybe make it clear. Wait, no, the display name can be "Joke Provider" but no, the user is Turkish, so maybe "Şaka Servisi" (Joke Service) is better? Yeah.

PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Kullanıcı şaka isteklerini karşılar, Türkçe ve İngilizce şakalar sunar." (Responds to user joke requests, offers Turkish and English jokes.)
PLUGIN_AUTHOR = "Electra Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []  # No external dependencies needed, we can have a built-in list of jokes.

Then PLUGIN_TRIGGERS: let's list all the Turkish phrases for asking a joke, plus English ones just in case. So:
PLUGIN_TRIGGERS = [
    "bana bir şaka yap",
    "şaka söyle",
    "bir şaka anlat",
    "şaka yap",
    "şaka ver",
    "tell me a joke",
    "say a joke",
    "give me a joke",
    "joke please"
]

PLUGIN_ROUTE_TOKEN = "JOKE"
PLUGIN_COMMANDS = ["/joke", "/şaka"]

Then the run function. Let's have a list of safe, family-friendly jokes, both Turkish and English. Wait, the original request was Turkish, so maybe prioritize Turkish jokes first. Let's make a list:

turkish_jokes = [
    "Çocuk: Anne, neden suyun içinde yürüyen balıklar yok?\nAnne: Çünkü onlar da yürüyüş yapmak için ayakkabı ister, oğlum.",
    "Adam bir restorana girer, garsona 'Bir su getir' der. Garson bir süre sonra gelir ve 'Suyunuz efendim' der. Adam 'Teşekkür ederim' der. Garson 'Rica ederim' der. Adam 'Ben söylemedim mi?' der. Garson 'Söylediniz efendim' der. Adam 'O haleyy benimki de söylendi demek?' der.",
    "Öğretmen: Ali, 2+2 kaç eder?\nAli: 4 efendim.\nÖğretmen: Çok iyi. Şimdi 4+2 kaç eder?\nAli: Aynı şey efendim, sıra bana gelmedi.",
    "Adamın biri taksi çevirir, şoföre 'En hızlı yoldan gidin, çok aciliyetim var' der. Şoför 5 dakika sonra arkasına döner ve 'Efendim, acil ne var?' diye sorar. Adam 'Benim taksi çağırdım, siz nereden geliyorsunuz?' der.",
    "Kedi ile köpek karşılaşır. Kedi: 'Nereye gidiyorsun?' Köpek: 'Evin sahibine gidiyorum, bana yemek verecek.' Kedi: 'Ben de evin sahibine gidiyorum, bana şaka anlatacak.'"
]

english_jokes = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call a fake noodle? An impasta!"
]

Then, in the run function, we can randomly pick one, maybe mix Turkish and English? Or if the prompt is in Turkish, pick a Turkish one? Wait, but maybe just randomly select from both, or have a mix. Also, make sure to handle any errors, like if random fails? No, random is built-in. Also, use context["print_fn"] if we want to show progressive output? Wait, no, the run function returns a string. Wait, but maybe if we want to show the joke nicely, but just returning the string is fine.

Wait, also, make sure that the run function doesn't crash. So wrap the joke selection in a try/except? Like, if for some reason the lists are empty, return a default joke.

Wait, let's write the run function:

import random
import os

def run(prompt: str, context: dict) -> str:
    try:
        # Check if prompt is in Turkish, prioritize Turkish jokes
        turkish_keywords = ["şaka", "anlat", "yap", "ver"]
        is_turkish = any(keyword in prompt.lower() for keyword in turkish_keywords)
        
        if is_turkish:
            joke = random.choice(turkish_jokes)
            prefix = "🎭 İşte senin için bir şaka:\n\n"
        else:
            joke = random.choice(english_jokes)
            prefix = "🎭 Here's a joke for you:\n\n"
        
        return f"{prefix}{joke}"
    except Exception as e:
        # Fallback joke if anything goes wrong
        return "🎭 Why did the plugin break? Because it couldn't handle the joke request! (Ama şimdi düzeldi, bir şaka daha ister misin?)"

Wait, that's good. Also, make sure that all the metadata is correct. Let's check the rules: PLUGIN_ENABLED is True, PLUGIN_TYPE is ROUTER, PLUGIN_REQUIRES is empty because we don't need any external packages, all jokes are built-in. The triggers cover the Turkish request "bana bir şaka yap" which is exactly what the user asked. The route token is JOKE, which is unique. The commands are /joke and /şaka, which are useful.

Wait, also, the module docstring? Oh right, the output should start with the module docstring or first import. Let's add a docstring at the top:

"""
Electra AI — Şaka Yapıcı Eklentisi
Kullanıcı şaka isteklerini karşılar, Türkçe ve İngilizce güvenli şakalar sunar.
"""
Then the imports: import random, then the metadata, then the joke lists, then the run function.

Wait, let's put it all together. Let's check for any issues: no hardcoded paths, uses context correctly, no external dependencies, handles errors, returns a non-empty string. The triggers include the exact phrase the user used: "bana bir şaka yap", so when the user asks that, the router will trigger this plugin.

Wait, also, make sure that the PLUGIN_TRIGGERS are all lowercase? Because the prompt is probably lowercased when matching? Yeah, the triggers are in lowercase, matching the user's request which is lowercase.

Wait, let's test: the user's request is "bana bir şaka yap" which is exactly in the PLUGIN_TRIGGERS list, so it will match. Perfect.

Also, the plugin is named autorepair_joke.py, which matches the token JOKE lowercase, so that's correct.

Wait, let's write the full code now, no markdown, just raw Python. Let's make sure there are no syntax errors. Let's check:

First the docstring, then imports, then metadata, then the joke lists, then the run function.

Wait, let's write it:

"""
Electra AI — Şaka Yapıcı Eklentisi
Kullanıcı şaka isteklerini karşılar, Türkçe ve İngilizce güvenli, aile dostu şakalar sunar.
"""
import random

PLUGIN_NAME = "Şaka Servisi"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Türkçe ve İngilizce şaka isteklerini karşılar, güvenli şakalar sunar."
PLUGIN_AUTHOR = "Electra Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = [
    "bana bir şaka yap",
    "şaka söyle",
    "bir şaka anlat",
    "şaka yap",
    "şaka ver",
    "tell me a joke",
    "say a joke",
    "give me a joke",
    "joke please"
]
PLUGIN_ROUTE_TOKEN = "JOKE"
PLUGIN_COMMANDS = ["/joke", "/şaka"]

# Güvenli, aile dostu şakalar
TURKISH_JOKES = [
    "Çocuk: Anne, neden suyun içinde yürüyen balıklar yok?\nAnne: Çünkü onlar da yürüyüş yapmak için ayakkabı ister, oğlum.",
    "Adam bir restorana girer, garsona 'Bir su getir' der. Garson bir süre sonra gelir ve 'Suyunuz efendim' der. Adam 'Teşekkür ederim' der. Garson 'Rica ederim' der. Adam 'Ben söylemedim mi?' der. Garson 'Söylediniz efendim' der. Adam 'O haleyy benimki de söylendi demek?' der.",
    "Öğretmen: Ali, 2+2 kaç eder?\nAli: 4 efendim.\nÖğretmen: Çok iyi. Şimdi 4+2 kaç eder?\nAli: Aynı şey efendim, sıra bana gelmedi.",
    "Adamın biri taksi çevirir, şoföre 'En hızlı yoldan gidin, çok aciliyetim var' der. Şoför 5 dakika sonra arkasına döner ve 'Efendim, acil ne var?' diye sorar. Adam 'Benim taksi çağırdım, siz nereden geliyorsunuz?' der.",
    "Kedi ile köpek karşılaşır. Kedi: 'Nereye gidiyorsun?' Köpek: 'Evin sahibine gidiyorum, bana yemek verecek.' Kedi: 'Ben de evin sahibine gidiyorum, bana şaka anlatacak.'",
    "Öğretmen: Ayşe, cümle içinde 'mutluluk' kelimesini kullan.\nAyşe: Annem yeni bir çorap aldı, çok mutluyum.\nÖğretmen: Neden mutlusun?\nAyşe: Çünkü artık tek çorap giymek zorunda değilim."
]

ENGLISH_JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look sad? Because it had too many problems."
]

def run(prompt: str, context: dict) -> str:
    try:
        # Türkçe istekleri algıla, Türkçe şakalar öncelikli
        turkish_keywords = ["şaka", "anlat", "yap", "ver", "bana bir"]
        is_turkish = any(keyword in prompt.lower() for keyword in turkish_keywords)
        
        if is_turkish:
            selected_joke = random.choice(TURKISH_JOKES)
            response_prefix = "🎭 İşte senin için bir şaka:\n\n"
        else:
            selected_joke = random.choice(ENGLISH_JOKES)
            response_prefix = "🎭 Here's a joke for you:\n\n"
        
        # İsteğe bağlı olarak Rich formatında çıktı vermek için print_fn kullanılabilir
        if "print_fn" in context and callable(context["print_fn"]):
            context["print_fn"](f"{response_prefix}{selected_joke}")
        
        return f"{response_prefix}{selected_joke}"
    except Exception as e:
        fallback_joke = "🎭 Neden eklenti şaka yapamadı? Çünkü şaka kodunu yanlış yazmış! (Ama şimdi düzeldi, bir şaka daha ister misin?)"
        if "print_fn" in context and callable(context["print_fn"]):
            context["print_fn"](fallback_joke)
        return fallback_joke

Wait, that's perfect. Let's check all the rules:

- PLUGIN_ENABLED is True: yes.
- PLUGIN_TYPE is ROUTER: yes.
- PLUGIN_REQUIRES is empty, no external deps: yes.
- Triggers include the exact user request "bana bir şaka yap": yes.
- PLUGIN_ROUTE_TOKEN is JOKE, unique: yes.
- run function returns non-empty string: yes.
- Uses context["print_fn"] if available: yes, that's good for progressive output in the GUI.
- Wraps everything in try/except: yes, so no crashes.
- No hardcoded paths: yes, no paths used at all.
- No imports from ai_terminal: yes, only imports random which is standard.
- The jokes are safe, family-friendly: yes.
- Handles both Turkish and English requests: yes, which is good for flexibility.

Wait, also, the user's request was in Turkish, so the Turkish jokes are prioritized, which is correct. The fallback joke is also in Turkish, which matches the user's language.

Is there anything missing? Let's check the plugin spec again. Oh, the metadata is all there: PLUGIN_NAME, VERSION, DESCRIPTION, AUTHOR, ENABLED, TYPE, REQUIRES, TRIGGERS, ROUTE_TOKEN, COMMANDS. All present.

The run function takes prompt and context, returns a string. Correct.

No external dependencies, so PLUGIN_REQUIRES is empty, which is fine.

The file will be named autorepair_joke.py, which is correct for the JOKE token.

Yes, this should work. Let's make sure there are no syntax errors. Let's check: the lists are properly formatted, the function is correctly defined, all variables are correctly named. Yep.

Wait, the docstring is at the top, which is fine. The imports are after the docstring, which is correct.

Another thing: the jokes are all appropriate, no offensive content, which is important for a general use plugin.

Also, the fallback joke is funny and in Turkish, which matches the user's request language.

Perfect. That's the plugin.
</think>

"""
Electra AI — Şaka Yapıcı Eklentisi
Kullanıcı şaka isteklerini karşılar, Türkçe ve İngilizce güvenli, aile dostu şakalar sunar.
"""
import random

PLUGIN_NAME = "Şaka Servisi"
PLUGIN_VERSION = "1.0.0"
PLUGIN_DESCRIPTION = "Türkçe ve İngilizce şaka isteklerini karşılar, güvenli şakalar sunar."
PLUGIN_AUTHOR = "Electra Community"
PLUGIN_ENABLED = True
PLUGIN_TYPE = "ROUTER"
PLUGIN_REQUIRES = []
PLUGIN_TRIGGERS = [
    "bana bir şaka yap",
    "şaka söyle",
    "bir şaka anlat",
    "şaka yap",
    "şaka ver",
    "tell me a joke",
    "say a joke",
    "give me a joke",
    "joke please"
]
PLUGIN_ROUTE_TOKEN = "JOKE"
PLUGIN_COMMANDS = ["/joke", "/şaka"]

# Güvenli, aile dostu şakalar
TURKISH_JOKES = [
    "Çocuk: Anne, neden suyun içinde yürüyen balıklar yok?\nAnne: Çünkü onlar da yürüyüş yapmak için ayakkabı ister, oğlum.",
    "Adam bir restorana girer, garsona 'Bir su getir' der. Garson bir süre sonra gelir ve 'Suyunuz efendim' der. Adam 'Teşekkür ederim' der. Garson 'Rica ederim' der. Adam 'Ben söylemedim mi?' der. Garson 'Söylediniz efendim' der. Adam 'O haleyy benimki de söylendi demek?' der.",
    "Öğretmen: Ali, 2+2 kaç eder?\nAli: 4 efendim.\nÖğretmen: Çok iyi. Şimdi 4+2 kaç eder?\nAli: Aynı şey efendim, sıra bana gelmedi.",
    "Adamın biri taksi çevirir, şoföre 'En hızlı yoldan gidin, çok aciliyetim var' der. Şoför 5 dakika sonra arkasına döner ve 'Efendim, acil ne var?' diye sorar. Adam 'Benim taksi çağırdım, siz nereden geliyorsunuz?' der.",
    "Kedi ile köpek karşılaşır. Kedi: 'Nereye gidiyorsun?' Köpek: 'Evin sahibine gidiyorum, bana yemek verecek.' Kedi: 'Ben de evin sahibine gidiyorum, bana şaka anlatacak.'",
    "Öğretmen: Ayşe, cümle içinde 'mutluluk' kelimesini kullan.\nAyşe: Annem yeni bir çorap aldı, çok mutluyum.\nÖğretmen: Neden mutlusun?\nAyşe: Çünkü artık tek çorap giymek zorunda değilim."
]

ENGLISH_JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised.",
    "Why don't skeletons fight each other? They don't have the guts.",
    "What do you call a fake noodle? An impasta!",
    "Why did the math book look sad? Because it had too many problems."
]

def run(prompt: str, context: dict) -> str:
    try:
        # Türkçe istekleri algıla, Türkçe şakalar öncelikli
        turkish_keywords = ["şaka", "anlat", "yap", "ver", "bana bir"]
        is_turkish = any(keyword in prompt.lower() for keyword in turkish_keywords)
        
        if is_turkish:
            selected_joke = random.choice(TURKISH_JOKES)
            response_prefix = "🎭 İşte senin için bir şaka:\n\n"
        else:
            selected_joke = random.choice(ENGLISH_JOKES)
            response_prefix = "🎭 Here's a joke for you:\n\n"
        
        # GUI'de progressive çıktı göstermek için print_fn kullan
        if "print_fn" in context and callable(context["print_fn"]):
            context["print_fn"](f"{response_prefix}{selected_joke}")
        
        return f"{response_prefix}{selected_joke}"
    except Exception as e:
        fallback_joke = "🎭 Neden eklenti şaka yapamadı? Çünkü şaka kodunu yanlış yazmış! (Ama şimdi düzeldi, bir şaka daha ister misin?)"
        if "print_fn" in context and callable(context["print_fn"]):
            context["print_fn"](fallback_joke)
        return fallback_joke