import Link from 'next/link';

const features = [
  {
    title: 'AI Clip Curation',
    detail: 'Find hook moments, story turns, and quotable segments with ranking signals optimized for short-form platforms.',
  },
  {
    title: 'Platform Presets',
    detail: 'Auto-generate 9:16 cuts for TikTok, Reels, and Shorts with caption-safe margins and headline overlays.',
  },
  {
    title: 'Virality Score',
    detail: 'See per-clip confidence with pace, emotional intensity, sentiment shifts, and engagement heuristics.',
  },
];

const workflow = [
  'Upload long-form video or podcast episode',
  'Transcribe and detect strongest story arcs',
  'Generate ranked clip candidates with hooks',
  'Export social-ready clips in one batch',
];

const clipRows = [
  { title: 'The shocking pivot moment', score: 92, length: '00:38', platform: 'TikTok + Reels' },
  { title: '3-step framework summary', score: 88, length: '00:52', platform: 'Shorts' },
  { title: 'Audience Q&A hot take', score: 84, length: '00:44', platform: 'All platforms' },
];

export default function Home() {
  return (
    <div className="space-y-16">
      <section className="grid gap-8 lg:grid-cols-[1.15fr_1fr] lg:items-center">
        <div className="space-y-6">
          <span className="badge">OpusClip-inspired workflow</span>
          <h1 className="text-4xl font-black tracking-tight text-white sm:text-6xl">
            Turn long videos into viral short clips in minutes.
          </h1>
          <p className="max-w-2xl text-lg text-zinc-300">
            This clone experience mimics the core OpusClip loop: upload content, auto-detect high-retention moments,
            and export captioned shorts ready to publish.
          </p>
          <div className="flex flex-wrap gap-3">
            <Link href="/register" className="rounded-xl bg-indigo-500 px-5 py-3 font-semibold text-white transition hover:bg-indigo-400">
              Create free workspace
            </Link>
            <Link href="/dashboard" className="rounded-xl border border-zinc-700 px-5 py-3 font-semibold text-zinc-100 transition hover:border-zinc-500">
              View product demo
            </Link>
          </div>
        </div>

        <div className="card space-y-4">
          <div className="flex items-center justify-between text-sm text-zinc-300">
            <span>Processing Session #4821</span>
            <span className="rounded bg-emerald-500/20 px-2 py-1 text-emerald-300">Live</span>
          </div>
          <div className="h-44 rounded-xl border border-zinc-800 bg-gradient-to-br from-zinc-800 to-zinc-900 p-4">
            <div className="text-sm text-zinc-400">Waveform + transcript alignment preview</div>
            <div className="mt-8 h-2 rounded bg-zinc-700">
              <div className="h-2 w-2/3 rounded bg-indigo-400" />
            </div>
          </div>
          <div className="grid grid-cols-3 gap-3 text-center text-sm">
            <div className="rounded-lg border border-zinc-800 bg-zinc-950 p-3">
              <div className="text-zinc-400">Candidates</div>
              <div className="mt-1 text-xl font-bold">24</div>
            </div>
            <div className="rounded-lg border border-zinc-800 bg-zinc-950 p-3">
              <div className="text-zinc-400">Avg Score</div>
              <div className="mt-1 text-xl font-bold">87</div>
            </div>
            <div className="rounded-lg border border-zinc-800 bg-zinc-950 p-3">
              <div className="text-zinc-400">Ready</div>
              <div className="mt-1 text-xl font-bold">11</div>
            </div>
          </div>
        </div>
      </section>

      <section className="space-y-6">
        <h2 className="section-title">Everything needed for an OpusClip-style pipeline</h2>
        <div className="grid gap-4 md:grid-cols-3">
          {features.map((feature) => (
            <article key={feature.title} className="card">
              <h3 className="text-xl font-bold text-white">{feature.title}</h3>
              <p className="mt-2 text-zinc-300">{feature.detail}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="grid gap-8 lg:grid-cols-2">
        <article className="card">
          <h2 className="section-title text-2xl">How it works</h2>
          <ol className="mt-5 space-y-3 text-zinc-200">
            {workflow.map((step, index) => (
              <li key={step} className="flex gap-3">
                <span className="mt-0.5 inline-flex h-6 w-6 flex-none items-center justify-center rounded-full bg-indigo-500/30 text-sm font-bold text-indigo-200">
                  {index + 1}
                </span>
                <span>{step}</span>
              </li>
            ))}
          </ol>
        </article>

        <article className="card">
          <h2 className="section-title text-2xl">Top clips this run</h2>
          <div className="mt-4 space-y-3">
            {clipRows.map((row) => (
              <div key={row.title} className="rounded-xl border border-zinc-800 bg-zinc-950 p-3">
                <div className="flex items-start justify-between gap-3">
                  <h3 className="font-semibold text-white">{row.title}</h3>
                  <span className="rounded-md bg-indigo-500/20 px-2 py-1 text-xs font-bold text-indigo-200">
                    Score {row.score}
                  </span>
                </div>
                <p className="mt-1 text-sm text-zinc-400">
                  {row.length} · {row.platform}
                </p>
              </div>
            ))}
          </div>
        </article>
      </section>
    </div>
  );
}
