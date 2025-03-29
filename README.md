# Wedding Planner API Flow

This document outlines the intended user interface flow and API endpoint interactions for the Wedding Planner application.

## User Interface Flow and API Endpoints

* **"Let's Start" Button:**
    * Clicking this button triggers a call to the `ask_wedding_date` endpoint.
* **"Ask Me" Button:**
    * Clicking this button triggers a call to the `ask_ai` endpoint.

**2. Setting Wedding Date:**

* **Date Input (Text Box):**
    * Users enter the wedding date in JSON format within a text box in the chat interface.
* **"Send" Button (Date):**
    * Clicking this button sends the JSON date input to the `set_wedding_date` endpoint.

**3. Setting Budget:**

* **Budget Input (Text Box):**
    * Users enter the wedding budget in JSON format within a text box in the chat interface.
* **"Send" Button (Budget):**
    * Clicking this button sends the JSON budget input to the `set_budget` endpoint.

**4. Selecting Wedding Vibes:**

* **"Continue" Button:**
    * Clicking this button triggers a call to the `ask_vibes` endpoint.
* **"Modify Manually" Button:**
    * Allows the user to manually enter or modify the vibes.
* **Vibe Banners:**
    * Each wedding vibe is displayed as a clickable banner.
    * Clicking a vibe banner triggers a call to the `set_vibes` endpoint.

**5. Selecting Venue:**

* **Venue Input (Text Box):**
    * Users enter the venue preference in JSON format within a text box in the chat interface.
* **"Send" Button (Venue):**
    * Clicking this button sends the JSON venue input to the `select_venue` endpoint.
* **Wedding Place Banners:**
    * Each wedding venue is displayed as a clickable banner.
    * Clicking a venue banner redirects the user to the venue's page.

**6. Managing Guest List and Invitations:**

* **"Manage Guest List" Button:**
    * Clicking this button redirects the user to the guest list management page.
* **"Select Invitation" Button:**
    * Clicking this button triggers a call to the `get_invitation_templates` endpoint.
* **Invitation Template Banners:**
    * Each invitation template is displayed as a clickable banner.
    * Clicking an invitation template banner triggers a call to the `set_invitation` endpoint.

**7. Finalization and AI Assistance:**

* **"Send" Button (Invitation):**
    * Clicking this button redirects the user to the finalized invitation page.
* **"Ask Me" Button:**
    * Clicking this button triggers a call to the `ask_ai` endpoint.