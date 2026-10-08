# Migration status — 2026-10-08
## Prepared — West Fork Creek / Project Omega landing page
Added a verified-information landing page at `/west-fork-creek` describing the West Fork Creek–Boeuf / Project Omega corridor and its related LPSC terminology (West Fork Creek–St. Landry). The page links to LPSC Docket U-37882, Order No. U-37882, public transmission testimony, Entergy’s project announcement, and the available interactive map. The page is prepared and locally checked; it is not yet deployed.
## Current state
Source committed to GitHub main at e3b92110d27a70fd794deea4c78da9fbe65e5a10 and confirmed by fetching origin/main. Netlify secure sign-in request returned declined on 2026-10-07; no deployment performed. Resume from authenticated Netlify access, not another rebuild.
Main live site remains Wix at https://www.winchlawfirm.com/. No DNS or specialty-site changes made.
Replacement rebuilt as static HTML/CSS/JS; Wix platform internals are not portable source. Existing main-page content and both published articles were retrieved from their live URLs, with sanitized source content in migration/.
Local build includes ten page routes (eight indexed), preserved article paths, landowner resource, resource directory, functional-form markup, static eagle, mobile menu, absolute share images/canonicals, robots/sitemap, old Entergy path redirects.
Homepage outcome-multiple language omitted from replacement; original remains in migration/home.html for review. Empty Wix booking service replaced with a consultation-request form, not a scheduling promise. Newsletter signup/member notifications are not migrated as services; legacy notifications redirects to contact.
## Verified locally
Build succeeds. Source link/metadata checks and JS syntax checks are recorded in tests/LOCAL_CHECKS.md. Browser rendering, Netlify form processing, notifications, and GA receipt are not verified.
## Exact blockers / launch gates
1. Netlify available browser is signed out. No Netlify plugin surfaced in discovery. Need authenticated account to create a separate main-site project connected to WINCHLAW/winchlawfirmwebsite, branch main, netlify.toml settings.
2. Enable form detection, deploy, configure consultation email notifications to justin.winch@winchlawfirm.com, and verify a synthetic request with dummy PDF reaches Netlify and firm inbox. Never assume delivery from an HTTP200 alone.
3. Correct GA4 property/measurement ID must be verified. Prior Windsor property417150352 returned no rows; user screenshot shows property555762522. Existing Wix public HTML did not reveal a GA measurement ID. GA_MEASUREMENT_ID is intentionally unset. Tracking code supports phone_click/email_click/specialty_site_click/consultation_start/generate_lead; GA receipt/key-event configuration pending.
4. Verify desktop and mobile preview, every preserved route, specialty link, images, form error states and no overflow. Article illustration should be archived at full resolution before retiring Wix.
5. Preserve email MX/TXT and all specialty-subdomain DNS; change only main web routing after gates pass. HTTPS certificate, www/apex redirect, canonical URL, and rollback must be tested.
6. Make a harmless repository change and observe the subsequent live Netlify deployment before claiming Git delivery works.
## Existing content
/ — main site
/louisiana-landowner-bill-of-rights — retained text
/legal-resources — directory enhanced with existing resources
/blog — both article links
/post/received-utility-right-of-way-offer-letter-louisiana — retained
/post/should-i-sign-utility-servitude-agreement-louisiana — retained
/book-online — consultation request instead of empty booking page
## Not part of this migration
Specialty sites are not modified. Their previously identified robots/sitemap, canonical/share metadata, intake/tracking issues remain a separate queue. Do not treat main migration as proof those sites work.
