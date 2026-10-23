-- Anonymous public discussion comments for the Zenith Hackers site.
-- Run once in Supabase Dashboard > SQL Editor for project xoptbtvgfenusohvqorh.
-- Visitors can post without accounts. New comments stay pending until approved in the dashboard.

create table if not exists public.visitor_comments (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  page_url text not null,
  display_name text not null,
  comment text not null,
  approved boolean not null default false
);

alter table public.visitor_comments enable row level security;
revoke all on table public.visitor_comments from anon, authenticated;
grant select, insert on table public.visitor_comments to anon;
grant usage, select on sequence public.visitor_comments_id_seq to anon;

drop policy if exists "Visitors can read approved comments" on public.visitor_comments;
create policy "Visitors can read approved comments"
on public.visitor_comments for select to anon
using (approved = true);

drop policy if exists "Visitors can submit pending comments" on public.visitor_comments;
create policy "Visitors can submit pending comments"
on public.visitor_comments for insert to anon
with check (
  approved = false
  and length(trim(page_url)) between 1 and 500
  and length(trim(display_name)) between 1 and 60
  and length(trim(comment)) between 2 and 2000
);

-- To approve a comment, open Table Editor > visitor_comments in Supabase
-- and set approved=true for that row. Never approve spam or personal information.
