-- Zenith Hackers consultation form: least-privilege public submission setup
-- Run once in Supabase Dashboard > SQL Editor for project xoptbtvgfenusohvqorh.
-- The public anon role can INSERT valid enquiries only; it cannot read, update, or delete submissions.

create table if not exists public.contact_submissions (
  id bigint generated always as identity primary key,
  created_at timestamptz not null default now(),
  name text not null,
  email text not null,
  service text not null,
  message text not null,
  consent boolean not null default false
);

alter table public.contact_submissions enable row level security;

revoke all on table public.contact_submissions from anon, authenticated;
grant insert on table public.contact_submissions to anon;
grant usage on sequence public.contact_submissions_id_seq to anon;

drop policy if exists "Public can submit consultation enquiries" on public.contact_submissions;
create policy "Public can submit consultation enquiries"
on public.contact_submissions
for insert
to anon
with check (
  consent = true
  and length(trim(name)) between 1 and 120
  and length(trim(email)) between 3 and 254
  and position('@' in email) > 1
  and length(trim(service)) between 1 and 100
  and length(trim(message)) between 1 and 2000
);

-- Intentionally do not create SELECT, UPDATE, or DELETE policies for anon.
-- View enquiries only from the authenticated Supabase Dashboard or a trusted backend.
