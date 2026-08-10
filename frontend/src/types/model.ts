export interface ModelInfo {

  id: string;

  name: string;

  version: string;

  media_type: string;

  architecture: string;

  framework: string;

  task: string;

  device: string;

  description: string;

  author: string;

  loaded: boolean;

}

export interface ModelsResponse {

  total_models: number;

  loaded_models: number;

  models: ModelInfo[];

}