const jobs = [
  { name: 'Creator Interview Masterclass.mp4', status: 'Analyzing transcript', progress: 72, eta: '2m left' },
  { name: 'Weekly Podcast Episode 118.mp4', status: 'Rendering top clips', progress: 49, eta: '6m left' },
  { name: 'UGC Product Demo.mov', status: 'Complete', progress: 100, eta: 'Done' },
];

const clips = [
  { title: '“This one tip changed everything”', score: 94, ratio: '9:16', captions: 'Dynamic', length: '00:34' },
  { title: 'Rapid-fire 3-point checklist', score: 90, ratio: '9:16', captions: 'Burned in', length: '00:45' },
  { title: 'Narrative pivot + emotional beat', score: 87, ratio: '9:16', captions: 'Animated', length: '00:41' },
  { title: 'Comment-reply style response', score: 83, ratio: '9:16', captions: 'Minimal', length: '00:29' },
];

export default function DashboardPage() {
  return (
    <div className="space-y-8">
      <section className="grid gap-4 md:grid-cols-4">
        <article className="card">
          <p className="text-sm text-zinc-400">Plan</p>
          <p className="mt-2 text-2xl font-bold text-white">Pro</p>
        </article>
        <article className="card">
          <p className="text-sm text-zinc-400">Uploads this month</p>
          <p className="mt-2 text-2xl font-bold text-white">18 / 30</p>
        </article>
        <article className="card">
          <p className="text-sm text-zinc-400">Clips exported</p>
          <p className="mt-2 text-2xl font-bold text-white">112</p>
        </article>
        <article className="card">
          <p className="text-sm text-zinc-400">Avg virality score</p>
          <p className="mt-2 text-2xl font-bold text-white">86.9</p>
        </article>
      </section>

      <section className="card space-y-5">
        <div className="flex flex-wrap items-center justify-between gap-3">
          <div>
            <h1 className="text-2xl font-black text-white">Processing queue</h1>
            <p className="text-zinc-400">Track uploads, transcript analysis, clip generation, and rendering.</p>
          </div>
          <button className="rounded-lg bg-indigo-500 px-4 py-2 text-sm font-semibold text-white hover:bg-indigo-400">
            + Upload new source
          </button>
        </div>

        <div className="space-y-3">
          {jobs.map((job) => (
            <article key={job.name} className="rounded-xl border border-zinc-800 bg-zinc-950 p-4">
              <div className="flex flex-wrap items-center justify-between gap-2">
                <h2 className="font-semibold text-white">{job.name}</h2>
                <span className="text-sm text-zinc-400">{job.eta}</span>
              </div>
              <p className="mt-1 text-sm text-zinc-300">{job.status}</p>
              <div className="mt-3 h-2 rounded-full bg-zinc-800">
                <div className="h-2 rounded-full bg-indigo-400" style={{ width: `${job.progress}%` }} />
              </div>
            </article>
          ))}
        </div>
      </section>

      <section className="card">
        <div className="flex items-center justify-between gap-3">
          <h2 className="text-2xl font-black text-white">Ranked clips</h2>
          <button className="rounded-lg border border-zinc-700 px-3 py-2 text-sm hover:border-zinc-500">Bulk export</button>
        </div>

        <div className="mt-5 overflow-x-auto">
          <table className="min-w-full text-left text-sm">
            <thead>
              <tr className="border-b border-zinc-800 text-zinc-400">
                <th className="py-3 pr-3">Title</th>
                <th className="py-3 pr-3">Score</th>
                <th className="py-3 pr-3">Length</th>
                <th className="py-3 pr-3">Aspect</th>
                <th className="py-3 pr-3">Captions</th>
                <th className="py-3">Action</th>
              </tr>
            </thead>
            <tbody>
              {clips.map((clip) => (
                <tr key={clip.title} className="border-b border-zinc-900">
                  <td className="py-3 pr-3 font-medium text-zinc-100">{clip.title}</td>
                  <td className="py-3 pr-3">
                    <span className="rounded bg-indigo-500/20 px-2 py-1 text-xs font-bold text-indigo-200">{clip.score}</span>
                  </td>
                  <td className="py-3 pr-3 text-zinc-300">{clip.length}</td>
                  <td className="py-3 pr-3 text-zinc-300">{clip.ratio}</td>
                  <td className="py-3 pr-3 text-zinc-300">{clip.captions}</td>
                  <td className="py-3">
                    <button className="rounded-md border border-zinc-700 px-2 py-1 text-xs hover:border-zinc-500">Preview</button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </section>
    </div>
  );
}
