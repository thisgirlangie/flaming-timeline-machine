<h2>Flaming Timeline Machine</h2>
Derived from Hackbright's <a href="http://chriszf.github.io/ratings/">Ratings</a> webapp using SQLAlchemy, Flask and Python.<br />

<h3>Tables</h3>
<strong>Students</strong><br />
id: integer (primary key)<br />
name: string<br />
headshot_img_url: string<br />
title_company: string<br />
hb_class: string<br />
<br />
<strong>Events</strong><br />
id: integer (primary key)<br />
title: string<br />
date: string<br />
description: string<br />
user_id: integer<br />
<br />
A <em>student</em> has many <em>events</em>.<br />
An <em>event</em> belongs to a <em>student</em>.<br />
<h3>Schema</h3>
<img src="schema_whiteboard.jpg">