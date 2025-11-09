from amirtapuri import amirtapuri_region_clg_teams, filter_by_institution_amirtapuri
from chennai import chennai_region_clg_teams, filter_by_institution_chennai
from cit import cit_clg_teams

if __name__ == "__main__":
    print("CIT Teams:")
    cit_clg_teams()
    print("\nChennai Region College Teams:")
    chennai_region_clg_teams()
    print("\nAmirtapuri Region College Teams:")
    amirtapuri_region_clg_teams()
    print("Filtered Teams by clg in Amirtapuri: ")
    filter_by_institution_amirtapuri(number_of_teams=1)
    print("Filtered Teams by clg in Chennai: ")
    filter_by_institution_chennai(number_of_teams=1)