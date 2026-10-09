# Migration and SEO status — October 9, 2026
## Current verified state
Main site is published at https://winchlawfirm.com/ on Netlify project majestic-cajeta-b5cfbd (50259f63-1a06-4d44-80b1-36fe24a8e725), with source WINCHLAW/winchlawfirmwebsite main.
Production deploy 6ac79c58b81b99000808ed1a published October8 at13:36:39Z from commit e30abec732b01da371378ef5fa3c0988bbaa2286, including West Fork Creek / Project Omega page.
Git delivery demonstrated again: commit72f68e5150f3342490e95df478ac882874993b58 triggered deploy6ac79e5d05635e0007af1d14, ready and published October8 at13:45:13Z.
Earlier notes claiming the main site remains on Wix, no Netlify plugin exists, or Git connection is unestablished are superseded. Do not rebuild or re-import the site. Publishing does not complete all acceptance gates.

## October 9 executed SEO improvement — Project Omega discovery
Evidence selected the homepage as the highest-value linking surface: GSC September11–October8 reports6 clicks/60 impressions/10% CTR/average position3.1667 for the HTTPS www homepage; GA4 property555762522 reports59 homepage landing sessions,45 active users and33 engaged sessions. The newly published West Fork Creek / Project Omega page had no homepage link.
Executed: added a visible Project Omega card in the homepage “Find your path” section linking to /west-fork-creek. Commit bb5b4120d37f8aa78902149741d75b5d0e4f685c triggered production deploy6ac8f063731a5900082d5fcb.
Verified live October9: deploy ready/published13:47:25Z; homepage card resolves to https://winchlawfirm.com/west-fork-creek; destination H1, canonical https://winchlawfirm.com/west-fork-creek, GTM container, dedicated expropriation phone and consultation links load. This internal-link task is complete.

## Today's executed repair — consultation capture
Before: live /book-online had Netlify form markup, but processing was disabled and get_forms returned[].
Executed: enabled Netlify Forms via authorized plugin; committed status change to trigger the connected build.
Verified: processing enabled; consultation form6ac79e68ad0ab40008f63ca1 registered at13:45:12Z, fields name/email/phone/topic/message/document/acknowledgment plus honeypot. Live HTML confirms Netlify processed the form. Dedicated expropriation phone504-377-2620 and general504-500-1899 remain distinct.
Synthetic test: POSTed a multipart consultation with a dummy PDF containing no client data, using the firm's own email. HTTP200, request01M4DW7YZBZH9K14GBKH0XX6ZA. Netlify last_submission_at changed to2026-10-08T13:46:31.986Z; verified submission_count remains0. Do not claim verified storage or upload retrieval. Possible spam filtering, not confirmed.
Outlook search from:formresponses@netlify.com received>=2026-10-08 returned no messages. This does not establish whether notifications are configured.
Exact remaining blocker: plugin exposes form metadata/count, not submission contents, spam classification, marking verified, or notification settings. Browser is signed out; this scheduled run cannot complete interactive authentication. Next action is inspect this single synthetic test in Forms > consultation > Spam/Verified submissions and verify its PDF and notification destination.
Concrete done condition: verified stored inquiry with retrievable dummy PDF, and receipt at justin.winch@winchlawfirm.com. Form detection is fixed; end-to-end delivery remains unfinished.

## Analytics evidence
Period September11–October8,2026; comparison August14–September10,2026.
GA4 requested property417150352 winchlawfirmgoogleanalytics: completed empty current and prior results, not proof of zero traffic.
Separately connected GA4 property555762522 Property1: homepage landing row59 sessions,45 active users,33 engaged sessions,55.93% engagement; /book-online1 session/0 engaged; /louisiana-landowner-bill-of-rights2 sessions/0 engaged; (not set)6 sessions. Source/medium report includes google/organic11 sessions,10 active users,10 engaged sessions; direct37 sessions,32 active users,10 engaged sessions. Event report returned133 page views,23 clicks,1 document_open and1 file_download; all returned key-event counts0 and no contact/consultation event row. Prior-period reads returned no rows; do not report percentage growth from an empty comparison.
GSC sc-domain:winchlawfirm.com recent period with provisional fresh data:
- HTTPS www homepage:6 clicks,60 impressions,10% CTR,average position3.1667.
- HTTPS Entergy homepage:0 clicks,13 impressions,0% CTR,position3.5385.
- HTTPS Babel homepage:0 clicks,2 impressions,0% CTR,position8.
- Historical HTTP Babel homepage:1 click,1 impression,position1; historical HTTP www homepage:0 clicks,2 impressions,position6.5.
Prior period returned no rows. Query report exposes3 clicks for 'justin winch'; remaining exposed queries are small-volume Abbeville legal terms with no clicks. Omitted/anonymized queries prevent classifying all page-level clicks. No identifiable visitors inferred.

## Prioritized queue
1. Main consultation form: repair executed and detection verified today; delivery/upload/spam/notification gate remains unfinished. Carry this gate forward, not repeat enabling detection.
2. Specialty social metadata: Entergy canonical and og:url now correctly https://entergy.winchlawfirm.com/; live og:image and twitter:image remain assets/og-cover.png. Babel canonical correctly https://entergybabelwebre.winchlawfirm.com/; Open Graph/Twitter tags absent. Prepared older files must be rebased onto latest live source before publishing to preserve October7 intake and Tag Manager changes. Entergy deploy6ac6d565094257480cd322be includes submit-review function and is not Git-backed per commit metadata.
3. Specialty robots/sitemaps: inspect actual public routes before composing/publishing.
4. GA property/stream reconciliation and live contact-event verification; do not remove existing Tag Manager based merely on absence of literal G-ID in HTML.
Navigation: Justin reported complete October2; specialty links verified October7. Do not repeat installation.
Main migration launch gates still pending: desktop/mobile rendering, all preserved routes/assets, end-to-end inquiry and upload receipt, notifications, GA receipt and key events, www/apex routing and preserved DNS/email records. Git deployment now verified.

## Creative candidate queue — research only
BREC Baton Rouge Zoo bald-eagle adoption: primary pages https://brzoo.org/support/adopt-an-animal and https://brzoo.org/animals/bald-eagle checked October8. Bald eagle listed; Go Green25 dollars/year, renewable, emailed certificate/keeper report/high-resolution photo. New planning detail: zoo says processing takes3–4 weeks. Species page does not identify resident bird's name, sex, individual story or current exhibit status. Commercial photo permission and public firm-adoption wording remain unverified.
Audience: Louisiana conservation/community families and potential local referrers; connection is the firm's eagle-and-land identity and actual regional conservation support, not a claim of legal referrals or ranking gains.
Next small action: retain this unsent question for a later authorized inquiry: 'Before Winch Law Firm adopts the bald eagle, can you confirm the resident bird's name/story/current exhibit status and whether the package photo may appear on a commercial firm website with credit? Is any public wording approval required?'
No outreach, spending, adoption or marketing publication performed. An outbound zoo link is a reference from our site; an independently earned inbound link is the zoo's separate editorial decision; a paid sponsorship link needs rel=sponsored or appropriate nofollow qualification. No backlink/endorsement/exclusivity promised.
Fair/show-pig candidate advanced October9: LSU AgCenter confirms the2027 State 4-H/FFA Livestock Show for February13–20,2027 at Lamar Dixon Expo Center in Gonzales. Its official sponsorship page supports the Livestock Youth Development Fund; published2026 major levels began at$2,500, which is outside the current inexpensive-candidate target. A prior Acadia Parish buckle sponsorship was$150, but the published deadline was November3,2025 and is stale—not a current offer. Next bounded action: watch for a2027 parish-level buckle/market-hog award opportunity at or below$250 before any outreach or spending. Audience is Louisiana 4-H/FFA exhibitors, agricultural families and rural referrers; the connection is real youth agricultural support, not a promised SEO link or endorsement.

## Preserved source/content
Existing main text and both articles retained in migration/ and generated routes.
/louisiana-landowner-bill-of-rights, /legal-resources, /blog,
/post/received-utility-right-of-way-offer-letter-louisiana,
/post/should-i-sign-utility-servitude-agreement-louisiana,
/book-online, /privacy, /thank-you, /west-fork-creek.
Static eagle, no splash animation. Newsletter/member notifications not migrated as services. Article illustration full-resolution archival before Wix retirement remains unverified.
