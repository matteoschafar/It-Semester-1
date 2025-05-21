def eingabe_der_werte():
    breite = float(input("Wie breit ist der Raum (in Metern)? "))
    laenge = float(input("Wie lang ist der Raum (in Metern)? "))
    hoehe = float(input("Wie hoch ist der Raum (in Metern)? "))
    t_innen = float(input("Innentemperatur (in °C)"))
    t_aussen = float(input("Außentemperatur (in °C)"))

    volumen = breite * laenge * hoehe
    dt = t_innen - t_aussen
    return volumen, dt

def berechne_heizleistung(l_volumen, l_dt):
    ergebnis = volumen * dt * 0.024
    return ergebnis

volumen, dt = eingabe_der_werte ()

if dt < 0:
    print(f"Achtung die Temperaturdifferenz ist kleiner als 0")

heizleistung = berechne_heizleistung(volumen, dt)
print(f"benötigte Heizleistung beträgt: {heizleistung}kw")