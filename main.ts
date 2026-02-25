import { verifyKey } from "https://deno.land/x/discordeno@18.0.1/mod.ts";

const PUBLIC_KEY = "ここにPublicKeyを貼る";

Deno.serve(async (req) => {
  if (req.method !== "POST") {
    return new Response("OK");
  }

  const signature = req.headers.get("x-signature-ed25519")!;
  const timestamp = req.headers.get("x-signature-timestamp")!;
  const body = await req.text();

  const isValid = await verifyKey(body, signature, timestamp, PUBLIC_KEY);
  if (!isValid) {
    return new Response("Invalid request", { status: 401 });
  }

  const interaction = JSON.parse(body);

  // Ping（必須）
  if (interaction.type === 1) {
    return new Response(JSON.stringify({ type: 1 }), {
      headers: { "Content-Type": "application/json" },
    });
  }

  // /hello
  if (interaction.type === 2 && interaction.data.name === "hello") {
    return new Response(
      JSON.stringify({
        type: 4,
        data: { content: "Hello from Deno 🚀" },
      }),
      { headers: { "Content-Type": "application/json" } }
    );
  }

  return new Response("Unknown interaction", { status: 400 });
});
