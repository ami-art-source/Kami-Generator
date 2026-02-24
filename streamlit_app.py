import streamlit as st

st.set_page_config(page_title="Grande Finale App", layout="centered")

st.title("🎉 Grande Finale – Generator • Konvertierer • Rechner")

# Tabs
tab1, tab2, tab3 = st.tabs(["🔮 Generator", "🔁 Konvertierer", "🧮 Rechner"])


# ---------------------------------------------------------
# TAB 1 – GENERATOR
# ---------------------------------------------------------
with tab1:
    st.header("🔮 Zufallsgenerator")

    gen_type = st.selectbox(
        "Was möchtest du generieren?",
        ["Zahl", "Text aus Liste", "Passwort"]
    )

    if gen_type == "Zahl":
        import random
        min_val = st.number_input("Minimum", value=1)
        max_val = st.number_input("Maximum", value=100)
        if st.button("Generieren"):
            st.success(f"Zufallszahl: {random.randint(min_val, max_val)}")

    elif gen_type == "Text aus Liste":
        import random
        items = st.text_area("Liste (ein Eintrag pro Zeile)").split("\n")
        if st.button("Zufälligen Eintrag wählen"):
            if items and items != [""]:
                st.success(f"Ausgewählt: {random.choice(items)}")
            else:
                st.error("Bitte gib mindestens einen Eintrag ein.")

    elif gen_type == "Passwort":
        import random, string
        length = st.slider("Passwortlänge", 4, 40, 12)
        if st.button("Passwort generieren"):
            chars = string.ascii_letters + string.digits + "!$%&/()=?"
            pw = "".join(random.choice(chars) for _ in range(length))
            st.success(f"🔐 Passwort: {pw}")


# ---------------------------------------------------------
# TAB 2 – KONVERTIERER
# ---------------------------------------------------------
with tab2:
    st.header("🔁 Einheiten‑Konvertierer")

    conv_type = st.selectbox(
        "Was möchtest du konvertieren?",
        ["Länge (m ↔ km)", "Gewicht (kg ↔ g)", "Temperatur (°C ↔ °F)"]
    )

    if conv_type == "Länge (m ↔ km)":
        meters = st.number_input("Meter eingeben", value=0.0)
        if st.button("Umrechnen (m → km)"):
            st.success(f"{meters} m = {meters / 1000} km")
        km = st.number_input("Kilometer eingeben", value=0.0)
        if st.button("Umrechnen (km → m)"):
            st.success(f"{km} km = {km * 1000} m")

    elif conv_type == "Gewicht (kg ↔ g)":
        kg = st.number_input("Kilogramm eingeben", value=0.0)
        if st.button("Umrechnen (kg → g)"):
            st.success(f"{kg} kg = {kg * 1000} g")
        g = st.number_input("Gramm eingeben", value=0.0)
        if st.button("Umrechnen (g → kg)"):
            st.success(f"{g} g = {g / 1000} kg")

    elif conv_type == "Temperatur (°C ↔ °F)":
        c = st.number_input("°C eingeben", value=0.0)
        if st.button("Umrechnen (°C → °F)"):
            st.success(f"{c} °C = {c * 9/5 + 32} °F")
        f = st.number_input("°F eingeben", value=0.0)
        if st.button("Umrechnen (°F → °C)"):
            st.success(f"{(f - 32) * 5/9} °C")


# ---------------------------------------------------------
# TAB 3 – RECHNER
# ---------------------------------------------------------
with tab3:
    st.header("🧮 Wahrscheinlichkeits‑Rechner")

    st.subheader("Mindestens einer hat Blutgruppe X")

    blood_type = st.selectbox(
        "Blutgruppe wählen",
        ["A (43%)", "B (11%)", "AB (5%)", "O (41%)"]
    )

    probs = {
        "A (43%)": 0.43,
        "B (11%)": 0.11,
        "AB (5%)": 0.05,
        "O (41%)": 0.41
    }

    p = probs[blood_type]

    if st.button("Berechnen"):
        result = 1 - (1 - p)**3
        st.success(f"Wahrscheinlichkeit: {round(result * 100, 2)} %")
