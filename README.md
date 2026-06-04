# zad2_TC
Zadanie 2 z przedmiotu Technologie Chmurowe

W łańcuchu wykorzystano:

Wyzwalacze: manualny(workflow_dispatch) oraz po git push z tagiem zaczynającym się od "v"

Checkout: łączy pipeline z repo

qemu-action: przygotowanie qemu do kompilacji obrazu pod arm64

buildx-action: przygotowanie buildera do budowy obrazu wieloarchitekturowego

metadata-action: przygotowanie nazwy obrazu i tagu, tagujemy po SHA oraz po wersji podanej w tagu(jeśli istnieje)

login-action: logowanie do Docker Hub(w celu użycia przechowywanego tam cache) i do GHCR(w celu wysłania obrazu)

build-push-action: budowanie obrazu lokalnego w celu przeskanowania(tutaj budujemy tylko na amd64 w celu przyspieszenia działania łańcucha) 

trivy-action: przeskanowanie obrazu przez Trivy, w przypadku wykrytej podatności High bądź Critical zwraca on exit code 1 i kończy działanie łańcucha

W przypadku braku takowych podatności build-push-action jest wywołany jeszcze raz w celu zbudowania obrazu na obie architektury(amd64 i arm64) oraz wysłania go na GHCR.
