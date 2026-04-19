import path from "node:path";
import { fileURLToPath } from "node:url";

const currentDirectory = path.dirname(fileURLToPath(import.meta.url));

/** @type {import('next').NextConfig} */
const nextConfig = {
  webpack: (config) => {
    config.resolve.alias["react-router-dom"] = path.resolve(
      currentDirectory,
      "src/lib/react-router-dom.tsx",
    );
    return config;
  },
};

export default nextConfig;
