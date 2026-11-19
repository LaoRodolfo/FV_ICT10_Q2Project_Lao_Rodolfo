
from pyscript import document

# Stores the names of registered ICT Fairview Club members.
club_members = [
    "Rodolfo Lao",
    "Sabine Agacita",
    "Raven Denum",
    "Maria Coronel",
    "Lance Catu",
    "Jhoana Evangelista"
]

# Stores the success and rejection messages.
verification_messages = {
    True: "Congratulations, {candidate_name}! You are registered in the ICT Fairview Club.",
    False: "Sorry, {candidate_name}. Your name is not on the membership list."
}

# Verifies the candidate's membership.
def verify_candidate(event):

    # Retrieves the input values.
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()

    # Checks whether both fields contain information.
    if not first_name or not last_name:
        document.getElementById("result").innerText = (
            "Please enter both your first name and last name."
        )
        return

    # Combines and formats the candidate's name.
    candidate_name = f"{first_name} {last_name}"
    candidate_name = " ".join(candidate_name.split()).title()

    # Checks whether the candidate is registered.
    is_member = candidate_name in club_members

    # Selects the appropriate verification message.
    result_message = verification_messages[is_member].format(
        candidate_name=candidate_name
    )

    # Creates a copy of the original list.
    members_copy = club_members.copy()

    # Combines the original list and its copy.
    combined_members = club_members + members_copy

    # Records the candidate's name.
    candidate_records = []
    candidate_records.append(candidate_name)

    # Counts the candidate's appearances.
    membership_count = club_members.count(candidate_name)

    # Gets the total number of registered members.
    total_members = len(club_members)

    # Creates an alphabetically sorted copy.
    sorted_members = sorted(club_members)

    # Stores the candidate's information in a tuple.
    candidate_record = (candidate_name, is_member)

    # Unpacks the tuple.
    recorded_name, recorded_status = candidate_record

    # Performs comparison operations.
    member_count_check = total_members > 0
    candidate_count_check = membership_count >= 1
    name_check = recorded_name == candidate_name
    status_check = recorded_status != False

    # Identifies the data types.
    name_type = type(candidate_name)
    members_type = type(club_members)
    record_type = type(candidate_record)

    # Displays the verification result.
    document.getElementById("result").innerText = (
        f"{result_message}\n\n"
        f"Registered members: {total_members}"
    )
