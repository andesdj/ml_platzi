curl -X POST -u "apikey:UcdbijSBI1UTj0HOjNlLjmgbS4dYHnLL8VPTSEKRgNL1" \
--header "Content-Type: application/json" \
--header "Accept: application/json" \
--data-binary @profile.json \
"https://api.us-south.personality-insights.watson.cloud.ibm.com/instances/982d8333-69b8-4fc2-891f-833e24dd4215/v3/profile?version=2017-10-13&consumption_preferences=true&raw_scores=true"
