pragma solidity 0.8.7;

//	SPDX-License-Identifier: MIT
//	BT Mini - Project - Build a medical records application
//	Group members: Anuj Mutha, Nidhi Pati, Amit Purohit

contract PatientInfo {

struct Patient {

string id;

string name;

string phone;

string treatment;

}

Patient[20] PatientInfoArray;

uint i=0;

// Function to register a patient

function registerPatient(string memory _pat_id, string memory _name, string memory _phone, string memory _treatment) public returns(string memory) {

Patient memory patient = Patient(_pat_id, _name, _phone, _treatment); if(i > 20) {

return "Limit reached";

}

else {

PatientInfoArray[i] = patient;

i += 1;

return "Patient registered...";

}

}


// Function to display patient data

function getPatient(uint idx) public view returns(string memory){ Patient memory patient = PatientInfoArray[idx];

return string(bytes.concat("Patient id: ", bytes(patient.id), ", Name: ", bytes(patient.name), ", Phone: ", bytes(patient.phone), "Treatment: ", bytes(patient.treatment)));
 
}

}
